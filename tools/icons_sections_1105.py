"""Иконки робота sections (2026-11-05): 85 новых сюжетов — спортинвентарь, форма, плавание, музыка и танец.
Каждый сюжет проверен по icons-catalog/sheet-*.png и icons-src/subjects.txt (не повторяется)."""
import os, sys
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
f = lambda cx, cy, d=9, k=0.75, **kw: face(cx, cy, d=d, k=k, **kw)
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "icons-src")
R, OR, Y, G, B, P, V, BR, WH, GR = ("#E8654F", "#FF9A3D", "#FFD25E", "#7CD26E", "#5CB7F2", "#FF8FB8", "#A98BF0",
                                    "#C0732E", "#FFFFFF", "#B8BCCB")
WAVE = f'<path d="M0 100 Q16 92 32 100 T64 100 T96 100 T128 100 V128 H0Z" fill="#7FD3F7" {W(2.6)}/>'
sp = lambda *pts: "".join(sparkle(x, y, r) for x, y, r in pts)

I = {}
# ===================== «Китёнок» — плавание =====================
I["kitenok-anokhina"] = ("blue", "доска для плавания",
    f'<rect x="30" y="22" width="68" height="84" rx="30" fill="{Y}" {s()}/><rect x="50" y="30" width="28" height="10" rx="5" fill="#fff" {W(2.4)}/>'
    + f(64, 68) + sp((108, 28, 6), (20, 96, 5)))
I["kitenok-nekrasovka"] = ("teal", "аквапалка (нудл)",
    f'<path d="M14 92 Q64 20 114 46" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round"/>'
    f'<path d="M14 92 Q64 20 114 46" fill="none" stroke="{P}" stroke-width="16" stroke-linecap="round"/>'
    f'<path d="M24 80 Q64 30 104 46" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
    + WAVE + f(62, 56, d=7, k=0.55))
I["kitenok-maryino"] = ("sky", "стартовая тумба",
    WAVE + f'<path d="M36 100 V60 H92 V100" fill="#9AA0B8" {s()}/><path d="M30 60 L40 44 H96 L92 60Z" fill="{R}" {s()}/>'
    f'<text x="64" y="94" font-family="Arial" font-weight="bold" font-size="18" text-anchor="middle" fill="#fff">1</text>'
    + f(64, 72, d=8, k=0.55, mouth=False))
I["kitenok-pechatniki"] = ("blue", "трамплин для прыжков в воду",
    WAVE + f'<path d="M16 100 V40 H34 V100" fill="#9AA0B8" {s()}/><path d="M16 40 H104 Q110 40 110 46 V50 H16Z" fill="{OR}" {s()}/>'
    f'<path d="M64 50 V60" {W(3)}/>' + f(80, 45, d=6, k=0.4, mouth=False) + sp((96, 20, 6)))
I["kitenok-tekstilshchiki"] = ("pink", "купальник",
    f'<path d="M44 18 L48 40 Q64 52 80 40 L84 18 L96 22 L90 56 Q88 72 98 104 Q64 92 30 104 Q40 72 38 56 L32 22Z" fill="#5CCDBA" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff"/>' for x, y in [(50, 80), (78, 84), (64, 94), (44, 60)]) + f(64, 66, d=8, k=0.55))
I["kitenok-kolomenskaya"] = ("sky", "плавки",
    f'<path d="M22 40 H106 L98 70 Q86 92 72 92 L64 76 L56 92 Q42 92 30 70Z" fill="{B}" {s()}/><path d="M22 48 H106" {W(2.6)}/>'
    f'<path d="M58 40 Q64 52 70 40" fill="none" {W(2.4)}/>' + f(64, 62, d=9, k=0.55) + sp((24, 98, 6), (106, 20, 5)))
I["kitenok-okskaya"] = ("orange", "полотенце",
    f'<path d="M28 24 H100 V96 H28Z" fill="#fff" {s()}/><path d="M28 36 H100 M28 84 H100" stroke="{R}" stroke-width="5"/>'
    f'<path d="M28 96 l4 10 M40 96 l0 10 M52 96 l0 10 M64 96 l0 10 M76 96 l0 10 M88 96 l0 10 M100 96 l-4 10" {W(2.4)}/>' + f(64, 60))
I["kitenok-likhobory"] = ("green", "шлёпанцы",
    "".join(f'<ellipse cx="{x}" cy="68" rx="20" ry="38" fill="{c}" {s()} transform="rotate({a} {x} 68)"/>'
            f'<path d="M{x-14} 50 Q{x} 66 {x+14} 50" fill="none" stroke="{Y}" stroke-width="7" transform="rotate({a} {x} 68)"/>'
            for x, c, a in [(42, R, -10), (86, B, 10)]) + f(42, 78, d=5, k=0.42) + f(86, 78, d=5, k=0.42))
I["kitenok-yasenevo"] = ("blue", "нарукавники",
    "".join(f'<rect x="{x}" y="34" width="34" height="58" rx="14" fill="{OR}" {s()}/><rect x="{x+8}" y="44" width="18" height="38" rx="8" fill="#BFE9FF" {W(2.4)}/>'
            for x in (20, 74)) + f(37, 102, d=5, k=0.4, blush=False) + f(91, 102, d=5, k=0.4, blush=False) + WAVE[:0] + sp((64, 26, 6)))
I["kitenok-molodezhnaya"] = ("teal", "мыло с пеной",
    f'<rect x="26" y="56" width="76" height="42" rx="18" fill="{P}" {s()}/>' + f(64, 76)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(2)}/>' for x, y, r in [(40, 44, 10), (58, 36, 12), (78, 42, 9), (92, 28, 7), (34, 24, 6)]))
I["kitenok-tushinskaya"] = ("purple", "банный халат",
    f'<path d="M40 18 L24 34 L14 74 L28 78 L34 56 V108 H94 V56 L100 78 L114 74 L104 34 L88 18 L64 44Z" fill="#fff" {s()}/>'
    f'<path d="M40 18 L64 44 L88 18 M64 44 V108 M34 72 H94" fill="none" {W(2.6)}/><path d="M34 72 H94" stroke="{P}" stroke-width="5"/>' + f(80, 92, d=6, k=0.42))
I["kitenok-nakhimovsky"] = ("sky", "поплавки-разделитель дорожек",
    f'<path d="M4 64 H124" {W(3)}/>' + "".join(f'<ellipse cx="{x}" cy="64" rx="11" ry="9" fill="{c}" {W(2.6)}/>' for x, c in
                                                [(12, R), (36, "#fff"), (60, R), (84, "#fff"), (108, R)])
    + WAVE + f(60, 63, d=4, k=0.32, blush=False) + sp((30, 30, 6), (98, 34, 5)))
I["kitenok-proletarskaya"] = ("blue", "душ",
    f'<path d="M30 110 V30 Q30 18 44 18 H70 V30" fill="none" {W(5)}/><path d="M50 30 H90 L84 46 H56Z" fill="{GR}" {s()}/>'
    + "".join(f'<path d="M{x} 54 L{x+dx} 96" stroke="#5CB7F2" stroke-width="3" stroke-linecap="round"/>' for x, dx in [(60, -6), (68, -2), (76, 2), (84, 6)])
    + f(70, 38, d=6, k=0.4, blush=False))
I["kitenok-filatov-lug"] = ("yellow", "флажки над бассейном",
    WAVE + f'<path d="M6 30 Q64 50 122 30" fill="none" {W(2.6)}/>'
    + "".join(f'<path d="M{x} {y} L{x+14} {y+2} L{x+6} {y+20}Z" fill="{c}" {W(2.2)}/>' for x, y, c in
              [(12, 33, R), (34, 38, "#fff"), (56, 40, R), (78, 39, "#fff"), (100, 35, R)]) + f(64, 76, d=8, k=0.55))
I["kitenok-salaryevo"] = ("green", "кепка-бейсболка",
    f'<path d="M24 74 Q24 30 64 30 Q100 30 102 74Z" fill="{R}" {s()}/><path d="M60 74 Q100 70 120 84 Q96 94 60 86Z" fill="#C8463A" {s()}/>'
    f'<circle cx="64" cy="30" r="5" fill="{R}" {W(2.4)}/>' + f(56, 56, d=8, k=0.55))
I["kitenok-rizhskaya"] = ("pink", "фен",
    f'<path d="M20 40 H82 Q100 40 100 56 Q100 72 82 72 H20Z" fill="{V}" {s()}/><path d="M50 72 L58 110 H74 L70 72" fill="{V}" {s()}/>'
    f'<path d="M12 40 V72" {W(4)}/>' + f(62, 56, d=8, k=0.5)
    + "".join(f'<path d="M{106} {y} Q114 {y-4} 122 {y}" fill="none" {W(2.4)}/>' for y in (46, 58, 70)))
I["kitenok-potapovo"] = ("teal", "расчёска",
    f'<rect x="18" y="40" width="92" height="26" rx="10" fill="{Y}" {s()}/>'
    + "".join(f'<path d="M{x} 66 V96" {W(4)}/>' for x in range(28, 104, 9)) + f(64, 53, d=8, k=0.42) + sp((104, 22, 6)))
I["kitenok-zhulebino"] = ("purple", "браслет-ключ от шкафчика",
    f'<ellipse cx="54" cy="58" rx="34" ry="28" fill="none" stroke="{O}" stroke-width="12"/><ellipse cx="54" cy="58" rx="34" ry="28" fill="none" stroke="{OR}" stroke-width="7"/>'
    f'<path d="M80 74 L100 98 M92 88 l8 -6 M98 96 l6 -5" {W(5)}/><circle cx="54" cy="30" r="12" fill="#fff" {W(2.6)}/>'
    f'<text x="54" y="35" font-family="Arial" font-weight="bold" font-size="13" text-anchor="middle" fill="{O}">7</text>' + f(54, 58, d=6, k=0.45))
I["kitenok-cheryomushki"] = ("yellow", "грамота",
    f'<rect x="24" y="20" width="80" height="88" rx="6" fill="#FFF8E6" {s()}/><path d="M24 20 H104 V32 H24Z" fill="{R}" {W(2.4)}/>'
    f'<path d="M38 74 H90 M38 84 H80" {W(2.6)}/><circle cx="86" cy="96" r="10" fill="{R}" {W(2.4)}/>' + f(64, 52, d=8, k=0.5))
I["kitenok-medvedkovo"] = ("night", "табло со счётом",
    f'<rect x="16" y="30" width="96" height="62" rx="10" fill="#2B2A44" {s()}/><path d="M64 38 V84" stroke="#555" stroke-width="2"/>'
    f'<text x="40" y="76" font-family="Arial" font-weight="bold" font-size="34" text-anchor="middle" fill="#FFD25E">2</text>'
    f'<text x="88" y="76" font-family="Arial" font-weight="bold" font-size="34" text-anchor="middle" fill="#7CD26E">1</text>'
    f'<path d="M40 92 V108 M88 92 V108" {W(4)}/>' + f(64, 22, d=5, k=0.38, blush=False))
I["kitenok-perovo"] = ("orange", "спортивная сумка",
    f'<path d="M44 44 Q44 22 64 22 Q84 22 84 44" fill="none" {W(5)}/><rect x="16" y="42" width="96" height="56" rx="22" fill="{B}" {s()}/>'
    f'<path d="M16 60 H112" stroke="#fff" stroke-width="4"/><circle cx="24" cy="70" r="6" fill="{Y}" {W(2)}/><circle cx="104" cy="70" r="6" fill="{Y}" {W(2)}/>' + f(64, 76))
I["kitenok-novogireevo"] = ("sky", "пьедестал почёта",
    f'<rect x="44" y="50" width="40" height="56" fill="{Y}" {s()}/><rect x="10" y="68" width="36" height="38" fill="{GR}" {s()}/>'
    f'<rect x="82" y="78" width="36" height="28" fill="{OR}" {s()}/>'
    f'<text x="28" y="96" font-family="Arial" font-weight="bold" font-size="18" text-anchor="middle" fill="#fff">2</text>'
    f'<text x="100" y="100" font-family="Arial" font-weight="bold" font-size="18" text-anchor="middle" fill="#fff">3</text>'
    + f(64, 76, d=7, k=0.5) + sp((64, 28, 9)))
I["kitenok-skhodnenskaya"] = ("green", "финишная лента",
    f'<path d="M14 30 V110 M114 30 V110" {W(5)}/><path d="M14 56 Q40 70 64 54 Q88 40 114 56" fill="none" stroke="{O}" stroke-width="12"/>'
    f'<path d="M14 56 Q40 70 64 54 Q88 40 114 56" fill="none" stroke="{R}" stroke-width="7"/>' + f(64, 88, d=8, k=0.55) + sp((40, 24, 6), (92, 24, 6)))

# ===================== «Мама, я плыву», «Аквакласс» — общий спортинвентарь =====================
I["mama-ya-plyvu-khodynka"] = ("blue", "гантель",
    f'<rect x="38" y="58" width="52" height="12" rx="4" fill="{GR}" {s()}/>'
    + "".join(f'<rect x="{x}" y="38" width="18" height="52" rx="7" fill="{P}" {s()}/>' for x in (18, 92))
    + "".join(f'<rect x="{x}" y="44" width="10" height="40" rx="4" fill="{P}" {W(2.4)}/>' for x in (34, 84)) + f(64, 46, d=7, k=0.42))
I["mama-ya-plyvu-shchelkovskaya"] = ("yellow", "аквапояс-поплавок",
    WAVE + f'<path d="M14 64 Q64 84 114 64" fill="none" {W(4)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="22" height="30" rx="7" fill="{c}" {s()}/>' for x, y, c in [(18, 52, B), (53, 60, OR), (88, 52, B)])
    + f(64, 73, d=5, k=0.38) + sp((30, 28, 6), (100, 26, 5)))
I["mama-ya-plyvu-kashirskaya"] = ("pink", "напульсник",
    f'<rect x="22" y="40" width="84" height="48" rx="20" fill="{G}" {s()}/><path d="M22 52 H106 M22 76 H106" stroke="#fff" stroke-width="5"/>' + f(64, 64))
I["mama-ya-plyvu-taganskaya"] = ("teal", "повязка на голову",
    f'<circle cx="64" cy="70" r="34" fill="#FFD9B8" {s()}/><path d="M30 58 Q64 40 98 58 L98 68 Q64 50 30 68Z" fill="{R}" {s()}/>'
    f'<path d="M98 60 L114 52 L110 66 L118 78 L100 70" fill="{R}" {W(2.6)}/>' + f(64, 80, d=10, k=0.6))
I["mama-ya-plyvu-otradnoe"] = ("orange", "эстафетная палочка",
    f'<rect x="20" y="52" width="88" height="24" rx="12" fill="{Y}" {s()}/><path d="M40 52 V76 M88 52 V76" stroke="{R}" stroke-width="5"/>'
    + f(64, 62, d=7, k=0.45) + "".join(f'<path d="M{x} {y} h-14" {W(3)}/>' for x, y in [(16, 46), (12, 64), (16, 82)]) + sp((104, 30, 6)))
I["mama-ya-plyvu-lukhmanovskaya"] = ("green", "беговой барьер",
    f'<path d="M26 108 V50 M102 108 V50 M18 108 H36 M94 108 H112" {W(4)}/>'
    f'<rect x="20" y="40" width="88" height="18" rx="4" fill="#fff" {s()}/>'
    + "".join(f'<rect x="{x}" y="40" width="14" height="18" fill="{R}"/>' for x in (28, 56, 84)) + f'<rect x="20" y="40" width="88" height="18" rx="4" fill="none" {s()}/>'
    + f(64, 80, d=8, k=0.5))
I["mama-ya-plyvu-dinamo"] = ("purple", "гимнастический мат",
    f'<path d="M14 70 L40 50 H114 L88 70Z" fill="{B}" {s()}/><path d="M14 70 H88 V96 H14Z" fill="#3E7FC8" {s()}/><path d="M88 70 L114 50 V76 L88 96Z" fill="#2E68A8" {s()}/>'
    f'<path d="M38 70 V96 M62 70 V96" stroke="#fff" stroke-width="2" opacity=".6"/>' + f(50, 83, d=8, k=0.5))
I["mama-ya-plyvu-vodny"] = ("sky", "гимнастические кольца",
    f'<path d="M40 6 V56 M88 6 V56" {W(3)}/><path d="M36 56 h8 v8 h-8z M84 56 h8 v8 h-8z" fill="{BR}" {W(2)}/>'
    + "".join(f'<circle cx="{x}" cy="84" r="17" fill="none" stroke="{O}" stroke-width="11"/><circle cx="{x}" cy="84" r="17" fill="none" stroke="{Y}" stroke-width="6"/>' for x in (40, 88))
    + f(64, 36, d=6, k=0.42))
I["aqua-class-rybalko"] = ("yellow", "турник",
    f'<path d="M20 112 V24 M108 112 V24" {W(5)}/><path d="M20 30 H108" stroke="{O}" stroke-width="8"/><path d="M20 30 H108" stroke="{GR}" stroke-width="4"/>'
    f'<circle cx="64" cy="62" r="14" fill="#FFD9B8" {s()}/><path d="M54 52 L50 30 M74 52 L78 30" {W(4)}/>' + f(64, 63, d=5, k=0.4)
    + f'<path d="M64 76 V96 M64 96 L56 110 M64 96 L72 110" {W(4)}/>')
I["pool-atlant"] = ("orange", "гимнастический козёл",
    f'<rect x="28" y="40" width="72" height="26" rx="12" fill="{BR}" {s()}/><path d="M40 66 L30 110 M88 66 L98 110 M44 66 L50 110 M84 66 L78 110" {W(5)}/>'
    + f(64, 53, d=8, k=0.5) + sp((104, 24, 6)))
I["pool-volna-chertanovo"] = ("blue", "спасательный шест",
    WAVE + f'<path d="M14 18 L96 96" stroke="{O}" stroke-width="10" stroke-linecap="round"/><path d="M14 18 L96 96" stroke="{R}" stroke-width="5" stroke-dasharray="10 10"/>'
    f'<path d="M96 96 Q112 96 112 80 Q112 70 102 70" fill="none" {W(5)}/>' + f(50, 50, d=6, k=0.4, blush=False))
I["pool-zorky"] = ("teal", "мяч для водного поло",
    WAVE + f'<circle cx="64" cy="64" r="36" fill="{Y}" {s()}/>'
    f'<path d="M30 52 Q64 64 98 52 M38 90 Q52 62 64 28 M90 90 Q76 62 64 28" fill="none" {W(2.6)}/>' + f(64, 70, d=8, k=0.5))
I["pool-arkhimed-dubna"] = ("sky", "весло",
    WAVE + f'<path d="M24 22 L92 90" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M24 22 L92 90" stroke="{BR}" stroke-width="5" stroke-linecap="round"/>'
    f'<path d="M80 78 Q100 70 112 92 Q104 112 84 104 Q76 96 80 78Z" fill="{OR}" {s()}/>' + f(96, 92, d=4, k=0.35, blush=False) + sp((96, 26, 7)))

# ===================== «Джигит.ру» — кавказские танцы и музыка =====================
I["djigit-mitino"] = ("night", "папаха",
    f'<path d="M24 76 Q20 30 64 28 Q108 30 104 76Z" fill="#F2F2F2" {s()}/>'
    + "".join(f'<path d="M{x} {y} q4 -6 8 0" fill="none" stroke="#B8BCCB" stroke-width="2.4"/>' for x, y in [(36, 46), (52, 40), (70, 40), (86, 48), (44, 60), (78, 60)])
    + f'<path d="M24 76 H104 V92 H24Z" fill="#3B3355" {s()}/>' + f(64, 104, d=8, k=0.5, blush=False))
I["djigit-baikalskaya"] = ("orange", "черкеска с газырями",
    f'<path d="M40 16 L22 30 L18 110 H110 L106 30 L88 16 L64 50Z" fill="#4A5068" {s()}/><path d="M64 50 V110" {W(2.6)}/>'
    + "".join(f'<rect x="{x}" y="{y}" width="5" height="12" rx="2" fill="{Y}" {W(1.6)}/>' for x in (30, 37, 44, 79, 86, 93) for y in (56,))
    + f'<path d="M24 92 H104" stroke="{Y}" stroke-width="4"/>' + f(64, 74, d=8, k=0.5))
I["djigit-komsomolskaya"] = ("yellow", "бубен",
    f'<circle cx="64" cy="64" r="40" fill="#FFF3D6" {s()}/><circle cx="64" cy="64" r="40" fill="none" stroke="{R}" stroke-width="8"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="{GR}" {W(2)}/>' for x, y in [(64, 20), (106, 64), (64, 108), (22, 64), (94, 34), (34, 94)]) + f(64, 64))
I["djigit-belyaevo"] = ("pink", "маракасы",
    "".join(f'<ellipse cx="{x}" cy="44" rx="18" ry="22" fill="{c}" {s()} transform="rotate({a} {x} 80)"/><rect x="{x-4}" y="64" width="8" height="40" rx="4" fill="{BR}" {s()} transform="rotate({a} {x} 80)"/>'
            for x, c, a in [(46, OR, -18), (82, G, 18)]) + f(40, 46, d=5, k=0.4) + f(88, 46, d=5, k=0.4))
I["djigit-altufyevo"] = ("teal", "кастаньеты",
    "".join(f'<path d="M{x} 40 Q{x+26} 40 {x+26} 68 Q{x+26} 98 {x} 98 Q{x-26} 98 {x-26} 68 Q{x-26} 40 {x} 40Z" fill="{c}" {s()}/>' for x, c in [(42, R), (88, "#A33A2E")])
    + f'<path d="M42 40 Q64 22 88 40" fill="none" stroke="{Y}" stroke-width="4"/>' + f(42, 70, d=6, k=0.45) + f(88, 70, d=6, k=0.45))
I["djigit-reutov"] = ("green", "гитара",
    f'<path d="M86 14 L74 52" stroke="{BR}" stroke-width="9" stroke-linecap="round"/><path d="M80 8 l12 4 -4 10 -12 -4z" fill="{O}"/>'
    f'<path d="M58 44 Q80 40 80 60 Q80 70 72 74 Q86 82 82 100 Q76 118 52 114 Q28 110 30 90 Q32 76 44 74 Q36 66 40 54 Q46 44 58 44Z" fill="{OR}" {s()}/>'
    f'<circle cx="60" cy="84" r="7" fill="{O}"/>' + f(56, 66, d=6, k=0.42))
I["djigit-bratislavskaya"] = ("purple", "труба",
    f'<path d="M14 64 H70" stroke="{O}" stroke-width="12" stroke-linecap="round"/><path d="M14 64 H70" stroke="{Y}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M66 64 L108 40 V88Z" fill="{Y}" {s()}/><path d="M34 64 V48 M46 64 V48 M58 64 V48" {W(4)}/>' + f(92, 64, d=5, k=0.4) + sp((24, 30, 6)))
I["djigit-shipilovskaya"] = ("blue", "саксофон",
    f'<path d="M50 14 Q60 14 60 24 V82 Q60 104 78 104 Q96 104 96 82 V72" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round"/>'
    f'<path d="M50 14 Q60 14 60 24 V82 Q60 104 78 104 Q96 104 96 82 V72" fill="none" stroke="{Y}" stroke-width="11" stroke-linecap="round"/>'
    f'<path d="M84 66 H108 L102 76 H90Z" fill="{Y}" {s()}/>' + "".join(f'<circle cx="60" cy="{y}" r="3.5" fill="#fff" {W(1.6)}/>' for y in (40, 52, 64))
    + f(78, 92, d=5, k=0.35, blush=False))
I["djigit-dmitriya-donskogo"] = ("yellow", "губная гармошка",
    f'<rect x="14" y="46" width="100" height="36" rx="8" fill="{GR}" {s()}/><rect x="14" y="58" width="100" height="12" fill="#fff" {W(2)}/>'
    + "".join(f'<rect x="{x}" y="60" width="6" height="8" fill="{O}"/>' for x in range(20, 110, 11)) + f(64, 48, d=8, k=0.4, mouth=False)
    + "".join(f'<path d="M{x} 30 l4 -10" {W(3)}/>' for x in (40, 64, 88)))
I["djigit-sosensky-stan"] = ("orange", "аккордеон",
    f'<rect x="12" y="34" width="28" height="64" rx="5" fill="{R}" {s()}/><rect x="88" y="34" width="28" height="64" rx="5" fill="{R}" {s()}/>'
    f'<path d="M40 38 L48 94 L56 38 L64 94 L72 38 L80 94 L88 38" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff"/>' for x in (20, 30) for y in (46, 58, 70, 82)) + f(102, 60, d=5, k=0.35, blush=False))
I["djigit-sochinskaya"] = ("green", "балалайка",
    f'<path d="M64 8 V60" stroke="{BR}" stroke-width="8" stroke-linecap="round"/><path d="M64 46 L104 108 H24Z" fill="{OR}" {s()}/>'
    f'<circle cx="64" cy="86" r="6" fill="{O}"/><path d="M60 14 V100 M68 14 V100" stroke="#fff" stroke-width="1.4" opacity=".8"/>' + f(64, 72, d=7, k=0.42))
I["djigit-odintsovo"] = ("sky", "метроном",
    f'<path d="M44 20 H84 L104 108 H24Z" fill="{BR}" {s()}/><path d="M50 40 H78 L88 92 H40Z" fill="#FFF3D6" {W(2.4)}/>'
    f'<path d="M64 92 L84 30" {W(3.5)}/><rect x="74" y="44" width="12" height="8" rx="2" fill="{R}" {W(2)} transform="rotate(18 80 48)"/>' + f(56, 76, d=5, k=0.38))
I["djigit-kirovogradskaya"] = ("purple", "наушники",
    f'<path d="M24 76 Q24 22 64 22 Q104 22 104 76" fill="none" stroke="{O}" stroke-width="12"/><path d="M24 76 Q24 22 64 22 Q104 22 104 76" fill="none" stroke="{P}" stroke-width="7"/>'
    + "".join(f'<rect x="{x}" y="62" width="26" height="40" rx="12" fill="{P}" {s()}/>' for x in (12, 90)) + f(64, 76, d=12, k=0.55))
I["djigit-polyarnaya"] = ("night", "виниловая пластинка",
    f'<circle cx="64" cy="64" r="44" fill="#2B2A44" {s()}/>' + "".join(f'<circle cx="64" cy="64" r="{r}" fill="none" stroke="#4A4970" stroke-width="2"/>' for r in (38, 32, 26))
    + f'<circle cx="64" cy="64" r="18" fill="{R}" {W(2.4)}/>' + f(64, 64, d=6, k=0.42) + sp((108, 22, 6)))
I["djigit-davydkovskaya"] = ("pink", "скрипичный ключ",
    f'<path d="M66 112 Q50 114 50 100 Q52 90 62 94 M66 112 L60 16 Q74 20 72 38 Q70 52 50 66 Q34 80 46 94 Q58 104 76 94 Q88 84 78 72 Q66 64 56 76" fill="none" stroke="{O}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M66 112 L60 16 Q74 20 72 38 Q70 52 50 66 Q34 80 46 94 Q58 104 76 94 Q88 84 78 72 Q66 64 56 76" fill="none" stroke="{V}" stroke-width="3.5" stroke-linecap="round"/>'
    + f(96, 40, d=5, k=0.35) + sp((28, 30, 7)))
I["djigit-vladimirskaya"] = ("teal", "камертон",
    f'<path d="M50 14 V60 Q50 76 64 76 Q78 76 78 60 V14" fill="none" stroke="{O}" stroke-width="12" stroke-linecap="round"/>'
    f'<path d="M50 14 V60 Q50 76 64 76 Q78 76 78 60 V14" fill="none" stroke="{GR}" stroke-width="7" stroke-linecap="round"/>'
    f'<path d="M64 76 V112" stroke="{O}" stroke-width="10" stroke-linecap="round"/>' + f(64, 52, d=6, k=0.38, blush=False)
    + "".join(f'<path d="M{x} {y} q6 6 0 12" fill="none" {W(2.4)}/>' for x, y in [(90, 24), (98, 18), (30, 24)]))
I["djigit-zhulebino"] = ("yellow", "арфа",
    f'<path d="M30 110 L36 20 Q70 14 100 50 Q90 70 96 110Z" fill="none" stroke="{O}" stroke-width="11" stroke-linejoin="round"/>'
    f'<path d="M30 110 L36 20 Q70 14 100 50 Q90 70 96 110Z" fill="none" stroke="{BR}" stroke-width="6" stroke-linejoin="round"/>'
    + "".join(f'<path d="M{x} {y} V108" stroke="#fff" stroke-width="2"/>' for x, y in [(46, 22), (56, 22), (66, 26), (76, 32), (86, 40)]) + f(64, 74, d=6, k=0.4))
I["djigit-nikulinskaya"] = ("blue", "музыкальный треугольник",
    f'<path d="M64 20 L104 96 H28" fill="none" stroke="{O}" stroke-width="9" stroke-linejoin="round"/><path d="M64 20 L104 96 H28" fill="none" stroke="{GR}" stroke-width="5" stroke-linejoin="round"/>'
    f'<path d="M64 10 V20" {W(2.4)}/><path d="M14 70 L52 50" stroke="{O}" stroke-width="4" stroke-linecap="round"/>' + f(66, 72, d=6, k=0.42))
I["djigit-shchukinskaya"] = ("orange", "граммофон",
    f'<rect x="30" y="80" width="56" height="28" rx="4" fill="{BR}" {s()}/><path d="M58 80 V60 Q60 46 72 44" fill="none" {W(5)}/>'
    f'<path d="M66 50 L96 12 Q118 20 116 46Z" fill="{Y}" {s()}/>' + f(58, 94, d=7, k=0.42)
    + "".join(f'<path d="M{x} {y} q6 -4 0 -10" fill="none" {W(2.2)}/>' for x, y in [(20, 50), (28, 36)]))

# ===================== танцевальные студии =====================
I["dancit-turistskaya"] = ("pink", "балетная пачка",
    f'<path d="M44 18 H84 L80 56 H48Z" fill="#FFC6DD" {s()}/><path d="M44 18 L52 10 M84 18 L76 10" {W(3)}/>'
    f'<path d="M48 56 Q14 60 10 74 Q40 80 64 78 Q88 80 118 74 Q114 60 80 56Z" fill="#fff" {s()}/>'
    f'<path d="M20 70 l8 -6 M40 72 l4 -8 M88 72 l-4 -8 M108 70 l-8 -6" {W(2)}/>' + f(64, 36, d=7, k=0.42) + sp((24, 26, 6), (104, 30, 5)))
I["vortex-dance"] = ("purple", "туфли для степа",
    f'<path d="M14 66 Q14 48 30 48 L48 50 Q56 62 76 64 L104 70 Q116 74 114 86 H14Z" fill="#2B2A44" {s()}/>'
    f'<path d="M14 86 H114 V94 H14Z" fill="{GR}" {s()}/><path d="M86 94 V102 H110 V94" fill="{GR}" {W(2.4)}/>'
    f'<path d="M50 56 L64 50 M56 60 L70 54" stroke="#fff" stroke-width="2.4"/>' + f(34, 66, d=5, k=0.38, blush=False) + sp((96, 34, 7), (70, 24, 5)))
I["dance-class-usievicha"] = ("night", "колонка-динамик",
    f'<rect x="32" y="14" width="64" height="100" rx="12" fill="{V}" {s()}/><circle cx="64" cy="40" r="12" fill="#2B2A44" {W(2.4)}/>'
    f'<circle cx="64" cy="84" r="22" fill="#2B2A44" {W(2.4)}/><circle cx="64" cy="84" r="9" fill="{P}"/>' + f(64, 40, d=5, k=0.32, blush=False)
    + "".join(f'<path d="M{x} {y} q8 8 0 16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' for x, y in [(104, 70), (112, 64)]))
I["dance-city-bibirevo"] = ("yellow", "галстук-бабочка",
    f'<path d="M58 64 L18 36 Q10 64 18 92Z" fill="{R}" {s()}/><path d="M70 64 L110 36 Q118 64 110 92Z" fill="{R}" {s()}/>'
    f'<rect x="54" y="52" width="20" height="24" rx="6" fill="#C8463A" {s()}/>' + f(64, 63, d=4, k=0.32, blush=False) + sp((30, 20, 6), (100, 108, 6)))

# ===================== «Школа мяча» — футбол =====================
I["schoolball-molodezhnaya"] = ("green", "футбольные ворота",
    f'<path d="M16 96 V34 H112 V96" fill="none" {W(5)}/>' + "".join(f'<path d="M{x} 34 V96" stroke="#fff" stroke-width="1.6"/>' for x in range(26, 112, 10))
    + "".join(f'<path d="M16 {y} H112" stroke="#fff" stroke-width="1.6"/>' for y in range(44, 96, 10)) + f'<path d="M8 100 H120" {W(3)}/>' + f(64, 66))
I["schoolball-pyatnitskoe"] = ("orange", "вратарские перчатки",
    "".join(f'<path d="M{x-18} 104 V60 Q{x-18} 40 {x-12} 34 V24 Q{x-6} 18 {x} 24 V30 Q{x+6} 22 {x+12} 30 V44 Q{x+20} 46 {x+18} 60 V104Z" fill="{c}" {s()}/>'
            f'<path d="M{x-18} 88 H{x+18}" stroke="#fff" stroke-width="5"/>' for x, c in [(42, G), (88, Y)]) + f(42, 66, d=5, k=0.4) + f(88, 66, d=5, k=0.4))
I["schoolball-novokosino"] = ("blue", "футбольные щитки",
    "".join(f'<path d="M{x-16} 24 H{x+16} Q{x+20} 70 {x} 106 Q{x-20} 70 {x-16} 24Z" fill="{c}" {s()}/>'
            f'<path d="M{x-10} 40 H{x+10}" stroke="#fff" stroke-width="3"/>' for x, c in [(42, OR), (86, R)]) + f(42, 64, d=5, k=0.4) + f(86, 64, d=5, k=0.4))
I["schoolball-ukhtomskaya"] = ("sky", "футбольные гетры",
    "".join(f'<path d="M{x} 14 H{x+24} V76 Q{x+24} 84 {x+32} 88 Q{x+40} 94 {x+34} 106 H{x+6} Q{x} 106 {x} 96Z" fill="{R}" {s()}/>'
            f'<path d="M{x} 26 H{x+24} M{x} 36 H{x+24}" stroke="#fff" stroke-width="4"/>' for x in (20, 66)) + f(32, 60, d=5, k=0.38) + f(78, 60, d=5, k=0.38))
I["schoolball-kotelniki"] = ("green", "угловой флажок",
    f'<path d="M40 112 V18" {W(5)}/><path d="M42 20 L102 34 L42 58Z" fill="{Y}" {s()}/><path d="M42 20 L72 27 L42 39Z" fill="{R}"/>'
    f'<path d="M10 108 Q40 84 74 108" fill="none" stroke="#fff" stroke-width="4"/>' + f(62, 36, d=5, k=0.38, blush=False))
I["schoolball-planernaya"] = ("purple", "карточки судьи",
    f'<rect x="22" y="24" width="48" height="70" rx="6" fill="{Y}" {s()} transform="rotate(-12 46 59)"/>'
    f'<rect x="58" y="32" width="48" height="70" rx="6" fill="{R}" {s()} transform="rotate(10 82 67)"/>' + f(82, 66, d=7, k=0.45))
I["schoolball-teply-stan"] = ("teal", "тактическая доска тренера",
    f'<rect x="18" y="24" width="92" height="76" rx="8" fill="#5FAF5A" {s()}/><path d="M64 24 V100" stroke="#fff" stroke-width="2.4"/><circle cx="64" cy="62" r="12" fill="none" stroke="#fff" stroke-width="2.4"/>'
    f'<path d="M30 40 l8 8 M38 40 l-8 8 M88 76 l8 8 M96 76 l-8 8" stroke="{Y}" stroke-width="3"/><path d="M42 78 Q60 90 80 50" fill="none" stroke="{Y}" stroke-width="3" stroke-dasharray="5 4"/>'
    + f(86, 44, d=5, k=0.32, blush=False))
I["schoolball-bibirevo"] = ("yellow", "насос для мяча",
    f'<rect x="50" y="40" width="28" height="68" rx="8" fill="{B}" {s()}/><path d="M64 40 V18 M48 18 H80" {W(5)}/>'
    f'<path d="M78 92 Q100 92 104 108" fill="none" {W(3.5)}/>' + f(64, 70, d=6, k=0.42))
I["schoolball-maryino"] = ("orange", "координационная лестница",
    f'<path d="M30 112 L50 16 M98 112 L78 16" {W(4)}/>' + "".join(f'<path d="M{30+20*t} {112-96*t} H{98-20*t}" stroke="{Y}" stroke-width="6"/>' for t in (0.1, 0.3, 0.5, 0.7, 0.9))
    + f(64, 64, d=6, k=0.38, blush=False))
I["schoolball-okskaya"] = ("sky", "скамейка запасных",
    f'<path d="M14 40 Q64 14 114 40 V60 H14Z" fill="#BFE9FF" opacity=".8" {s()}/><rect x="18" y="72" width="92" height="14" rx="4" fill="{R}" {s()}/>'
    f'<path d="M26 86 V106 M102 86 V106" {W(4)}/>' + f(64, 54, d=8, k=0.5))
I["schoolball-rimskaya"] = ("green", "капитанская повязка",
    f'<rect x="14" y="40" width="100" height="48" rx="14" fill="{Y}" {s()}/>'
    f'<text x="64" y="80" font-family="Arial" font-weight="bold" font-size="38" text-anchor="middle" fill="{O}">C</text>' + f(30, 64, d=4, k=0.32, blush=False) + sp((104, 24, 7)))
I["schoolball-altufyevo"] = ("pink", "стойки для обводки",
    "".join(f'<path d="M{x} {y} V108" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M{x} {y} V108" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
            for x, y, c in [(30, 30, Y), (64, 20, R), (98, 30, Y)]) + f'<path d="M14 110 H114" {W(3)}/>' + f(64, 64, d=8, k=0.45, blush=False)
    + f'<circle cx="46" cy="96" r="9" fill="#fff" {W(2.4)}/>')
I["schoolball-annino"] = ("blue", "сетка с мячами",
    f'<path d="M64 10 V30" {W(3)}/><path d="M40 30 H88 Q110 70 92 106 H36 Q18 70 40 30Z" fill="#fff" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="14" fill="{c}" {W(2.4)}/>' for x, y, c in [(52, 56, OR), (78, 58, G), (64, 86, Y)])
    + f'<path d="M30 50 L98 90 M98 50 L30 90 M40 30 L88 106 M88 30 L40 106" stroke="{O}" stroke-width="1.6" opacity=".7"/>' + f(64, 86, d=4, k=0.32, blush=False))
I["schoolball-bagrationovskaya"] = ("night", "табличка замены",
    f'<rect x="18" y="26" width="92" height="56" rx="8" fill="#2B2A44" {s()}/><rect x="56" y="82" width="16" height="28" rx="4" fill="{GR}" {s()}/>'
    f'<text x="40" y="66" font-family="Arial" font-weight="bold" font-size="24" text-anchor="middle" fill="#FF6B6B">7</text>'
    f'<text x="88" y="66" font-family="Arial" font-weight="bold" font-size="24" text-anchor="middle" fill="#7CE87C">9</text>'
    f'<path d="M58 48 h12 l-4 -4 M70 60 h-12 l4 4" stroke="{Y}" stroke-width="2.6" fill="none"/>' + f(64, 98, d=3, k=0.25, blush=False, mouth=False))
I["schoolball-krylatskoe"] = ("yellow", "вымпел",
    f'<path d="M30 16 H98" {W(4)}/><path d="M36 18 H92 V70 L64 110 L36 70Z" fill="{B}" {s()}/><path d="M36 30 H92" stroke="#fff" stroke-width="5"/>'
    f'<path d="M64 14 V6" {W(3)}/>' + f(64, 60, d=8, k=0.5) + f'<path d="M44 108 l-6 8 M84 108 l6 8" {W(2.4)}/>')
I["schoolball-kuzminki"] = ("teal", "спортивные шорты",
    f'<path d="M24 26 H104 L112 100 H72 L64 64 L56 100 H16Z" fill="{OR}" {s()}/><path d="M24 36 H104" {W(2.6)}/>'
    f'<path d="M18 86 H54 M74 86 H110" stroke="#fff" stroke-width="4"/>' + f(64, 48, d=8, k=0.45))
I["schoolball-leninsky"] = ("night", "стадионный прожектор",
    f'<path d="M64 60 V118 M50 118 H78" {W(5)}/><rect x="26" y="12" width="76" height="50" rx="6" fill="{GR}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#FFF7C2" {W(2)}/>' for x in (40, 64, 88) for y in (26, 48)) + f(64, 37, d=12, k=0.38, blush=False, mouth=False)
    + "".join(f'<path d="M{a} 66 L{b} 100" stroke="#FFF7C2" stroke-width="3" opacity=".7"/>' for a, b in [(30, 14), (98, 114)]))
I["schoolball-myakinino"] = ("purple", "эспандер",
    "".join(f'<rect x="{x}" y="28" width="22" height="46" rx="10" fill="{c}" {s()}/>' for x, c in [(16, B), (90, B)])
    + "".join(f'<path d="M38 {y} Q64 {y+24} 90 {y}" fill="none" stroke="{O}" stroke-width="7"/><path d="M38 {y} Q64 {y+24} 90 {y}" fill="none" stroke="{R}" stroke-width="3.5"/>' for y in (40, 58))
    + f(64, 98, d=8, k=0.45))
I["schoolball-novogireevo"] = ("sky", "спрей-заморозка",
    f'<rect x="40" y="38" width="48" height="74" rx="10" fill="{B}" {s()}/><rect x="52" y="22" width="24" height="16" rx="3" fill="#fff" {s()}/>'
    f'<path d="M76 28 H90" {W(4)}/><path d="M48 60 H80 M48 92 H80" stroke="#fff" stroke-width="4"/>' + f(64, 76, d=7, k=0.42)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" {W(1.4)}/>' for x, y, r in [(100, 22, 4), (110, 32, 3), (104, 14, 3)]))
I["schoolball-solntsevo"] = ("green", "волан для бадминтона",
    f'<path d="M50 20 L78 20 L92 78 H36Z" fill="#fff" {s()}/><path d="M56 20 L50 78 M64 20 V78 M72 20 L78 78" {W(2)}/><path d="M40 52 H88" {W(2)}/>'
    f'<path d="M36 78 H92 Q92 108 64 108 Q36 108 36 78Z" fill="{R}" {s()}/>' + f(64, 90, d=7, k=0.42))
I["schoolball-fiztekh"] = ("orange", "ракетка для настольного тенниса",
    f'<rect x="56" y="74" width="16" height="40" rx="6" fill="{BR}" {s()}/><circle cx="64" cy="52" r="36" fill="{R}" {s()}/>'
    + f(64, 52) + f'<circle cx="104" cy="96" r="8" fill="#fff" {W(2.4)}/>')

# ===================== бокс и теннис =====================
I["dynamo-boxing-arena"] = ("pink", "боксёрская перчатка",
    f'<path d="M40 30 Q40 14 64 14 H76 Q102 14 102 44 V66 Q102 80 88 82 H44 Q34 82 34 70 V50 Q26 48 28 38 Q32 30 40 30Z" fill="{R}" {s()}/>'
    f'<rect x="42" y="82" width="50" height="26" rx="6" fill="#fff" {s()}/><path d="M50 95 H84" stroke="{R}" stroke-width="3"/>' + f(70, 48))
I["dynamo-boxing-ramenki"] = ("blue", "боксёрский шлем",
    f'<path d="M24 78 Q22 20 64 18 Q106 20 104 78 Q104 104 86 108 V76 H42 V108 Q24 104 24 78Z" fill="{B}" {s()}/>'
    f'<path d="M42 50 H86 V76 H42Z" fill="#FFD9B8" {s()}/>' + f(64, 60, d=8, k=0.45) + f'<path d="M36 30 Q64 20 92 30" fill="none" stroke="#fff" stroke-width="3"/>')
I["dynamo-boxing-volley-arena"] = ("yellow", "боксёрский ринг",
    f'<path d="M10 92 L30 68 H98 L118 92Z" fill="#9FD8FF" {s()}/><path d="M10 92 H118 V104 H10Z" fill="#3E7FC8" {s()}/>'
    f'<path d="M14 92 V44 M114 92 V44 M32 68 V30 M96 68 V30" {W(4)}/>'
    + "".join(f'<path d="M14 {y} L32 {y-14} H96 L114 {y}" fill="none" stroke="{c}" stroke-width="3.5"/>' for y, c in [(52, R), (64, "#fff"), (76, B)])
    + f(64, 82, d=7, k=0.4))
I["tennis-borodina-kapitoliy"] = ("green", "теннисная ракетка",
    f'<path d="M64 74 L64 118" stroke="{O}" stroke-width="12" stroke-linecap="round"/><path d="M64 74 L64 118" stroke="{BR}" stroke-width="7" stroke-linecap="round"/>'
    f'<ellipse cx="64" cy="44" rx="30" ry="36" fill="#fff" {s()}/>'
    + "".join(f'<path d="M{x} 12 V76" stroke="{GR}" stroke-width="1.6"/>' for x in range(42, 90, 8))
    + "".join(f'<path d="M34 {y} H94" stroke="{GR}" stroke-width="1.6"/>' for y in range(20, 74, 8))
    + f'<ellipse cx="64" cy="44" rx="30" ry="36" fill="none" stroke="{O}" stroke-width="7"/><ellipse cx="64" cy="44" rx="30" ry="36" fill="none" stroke="{V}" stroke-width="3.5"/>'
    + f(64, 44, d=8, k=0.45))
I["tennis-borodina-degunino"] = ("teal", "ракетка для падела",
    f'<rect x="56" y="80" width="16" height="36" rx="6" fill="#2B2A44" {s()}/><path d="M30 46 Q30 12 64 12 Q98 12 98 46 Q98 80 64 86 Q30 80 30 46Z" fill="{OR}" {s()}/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#fff" {W(1.4)}/>' for x in (48, 64, 80) for y in (28, 66))
    + f(64, 46, d=8, k=0.45))

if __name__ == "__main__":
    ids = sys.argv[1:] or list(I)
    for pid in ids:
        bg, subj, body = I[pid]
        open(os.path.join(out, f"{pid}.svg"), "w").write(svg(bg, body))
    print("svg:", len(ids))
