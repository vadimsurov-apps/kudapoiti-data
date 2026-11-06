"""Кафе с детской (06.11): перерисовка непонятных иконок (кухонная техника, сырые овощи, экзотические фрукты, утварь).
Якорь — готовое блюдо-персонаж крупно; у сети — фирменное блюдо во всех филиалах (узнаваемость), у филиала — свой
крупный понятный аксессуар (шутка). Уникальна пара «блюдо + аксессуар». Понятные иконки (тако, брауни, чебурек…) не трогаем."""
import json, math, os, re
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
F = lambda x, y, d=8, k=0.7, **kw: face(x, y, d=d, k=k, **kw)

# ---------- блюда: (svg, центр лица, верх головы для шапок, полуширина) ----------

def roll():   # ролл
    return (f'<circle cx="64" cy="70" r="36" fill="#2E3A46" {s()}/><circle cx="64" cy="70" r="29" fill="#fff" {W(2)}/>'
            f'<circle cx="64" cy="70" r="12" fill="#FF8A5C" {W(2)}/><path d="M58 64 L70 76 M70 64 L58 76" stroke="#7CD26E" stroke-width="3"/>'
            + F(64, 88, d=8, k=0.55, blush=True)), 34, 30

def pizza():
    return (f'<path d="M28 34 Q64 18 100 34 L64 114Z" fill="#FFD25E" {s()}/><path d="M28 34 Q64 18 100 34 Q64 30 28 34Z" fill="#E0A830" {W(3)}/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#E8554A" {W(1.6)}/>' for x, y in [(50, 46), (78, 48), (64, 84)])
            + F(64, 62, d=8, k=0.6)), 22, 36

def pasta():
    return (f'<path d="M22 66 H106 Q104 106 64 106 Q24 106 22 66Z" fill="#fff" {s()}/>'
            f'<path d="M30 66 Q34 44 50 52 Q56 36 70 46 Q84 36 90 52 Q102 50 98 66" fill="#FFE07A" {W(2.6)}/>'
            f'<path d="M40 60 Q50 54 60 60 M66 58 Q76 50 88 60" fill="none" stroke="#E0A830" stroke-width="2.4"/>'
            f'<circle cx="64" cy="48" r="5" fill="#E8554A" {W(1.6)}/>' + F(64, 84, d=9, k=0.65)), 38, 42

def plov():   # горка риса с морковкой на синем ляганe
    return (f'<ellipse cx="64" cy="94" rx="52" ry="14" fill="#3E9BE0" {s()}/><ellipse cx="64" cy="92" rx="38" ry="8" fill="#9ED3FF"/>'
            f'<path d="M22 92 Q26 46 64 44 Q102 46 106 92Z" fill="#FFF3D6" {s()}/>'
            + "".join(f'<rect x="{x}" y="{y}" width="12" height="4" rx="2" fill="#FF8A3D" {W(1.2)} transform="rotate({a} {x} {y})"/>' for x, y, a in [(36, 66, 25), (84, 58, -20), (56, 52, 10), (88, 80, 30), (30, 82, -25), (70, 54, -10)])
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.3" fill="#E0C8A0"/>' for x, y in [(46, 58), (78, 70), (40, 74), (94, 70), (60, 86), (50, 70)])
            + F(64, 74, d=10, k=0.7)), 42, 40

def teapot():
    return (f'<path d="M30 70 Q30 40 64 40 Q98 40 98 70 Q98 104 64 104 Q30 104 30 70Z" fill="#4FB0E8" {s()}/>'
            f'<path d="M98 62 Q118 60 116 80 Q110 92 98 88" fill="none" {W(5)}/><path d="M30 64 L14 50 L18 46 L34 58" fill="#4FB0E8" {W(3)}/>'
            f'<ellipse cx="64" cy="40" rx="18" ry="6" fill="#fff" {W(3)}/><circle cx="64" cy="31" r="5" fill="#fff" {W(2.4)}/>'
            f'<path d="M40 82 Q64 92 88 82" fill="none" stroke="#fff" stroke-width="4"/>' + F(64, 66, d=10, k=0.7)), 26, 34

def vareniki():
    return (f'<path d="M14 78 Q14 40 62 42 Q62 82 14 78Z" fill="#FFF3D6" {s()}/>'
            f'<path d="M50 96 Q48 50 106 54 Q110 98 50 96Z" fill="#FFF3D6" {s()}/>'
            f'<path d="M54 92 Q56 62 102 58" fill="none" stroke="#E0C8A0" stroke-width="3" stroke-dasharray="4 5"/>'
            f'<ellipse cx="34" cy="50" rx="8" ry="4" fill="#fff" {W(1.6)}/>' + F(80, 78, d=9, k=0.65)), 52, 32

def khinkali():
    return (f'<path d="M24 92 Q24 52 64 36 Q104 52 104 92 Q64 104 24 92Z" fill="#FFF3D6" {s()}/>'
            + "".join(f'<path d="M64 36 Q{64+dx*0.6:.0f} 60 {64+dx} 92" fill="none" stroke="#E0C8A0" stroke-width="2.4"/>' for dx in (-30, -15, 15, 30))
            + f'<path d="M58 36 Q64 18 70 36Z" fill="#FFF3D6" {W(3)}/>' + F(64, 74, d=9, k=0.65)), 22, 40

def cheese():   # клинышек сыра с дырочками, лицо на боку
    return (f'<path d="M14 82 L96 44 L116 58 L34 96Z" fill="#FFE07A" {s()}/><path d="M34 96 L116 58 V96 Q116 104 108 104 H40 Q34 104 34 98Z" fill="#FFC93C" {s()}/>'
            f'<path d="M14 82 L34 96 V104 L14 90Z" fill="#E0A830" {W(2.6)}/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E0A830"/>' for x, y, r in [(58, 66, 5), (84, 56, 4), (108, 76, 4), (46, 98, 3)])
            + F(76, 86, d=9, k=0.65)), 46, 40

def burger():
    return (f'<path d="M24 64 Q24 32 64 32 Q104 32 104 64Z" fill="#E0A830" {s()}/>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="2" ry="3" fill="#fff"/>' for x, y in [(50, 42), (64, 38), (78, 44), (58, 50)])
            + f'<path d="M20 66 Q32 74 44 66 Q56 74 68 66 Q80 74 92 66 Q104 74 108 66" fill="#7CD26E" {W(2.4)}/>'
            f'<rect x="22" y="72" width="84" height="12" rx="6" fill="#8A5530" {W(2.6)}/><path d="M22 88 H106 Q106 104 64 104 Q22 104 22 88Z" fill="#E0A830" {s()}/>'
            + F(64, 54, d=10, k=0.6, blush=False)), 30, 42

def pancakes():
    return ("".join(f'<ellipse cx="64" cy="{y}" rx="40" ry="10" fill="#F2B866" {W(2.6)}/>' for y in (98, 86, 74, 62))
            + f'<path d="M30 60 Q34 76 46 70 Q52 84 60 70 Q72 82 80 68 Q92 78 98 60" fill="#A8522B" {W(2)}/>'
            + f'<rect x="54" y="44" width="20" height="12" rx="3" fill="#FFF3A0" {W(2.4)}/>' + F(64, 86, d=10, k=0.6)), 42, 42

def cupcake():
    return (f'<path d="M34 70 H94 L86 108 H42Z" fill="#5CB7F2" {s()}/>'
            + "".join(f'<path d="M{x} 72 L{x+2} 106" stroke="#fff" stroke-width="2"/>' for x in (46, 58, 70, 82))
            + f'<path d="M30 72 Q26 50 48 50 Q50 32 64 34 Q78 32 80 50 Q102 50 98 72Z" fill="#FFB3CF" {s()}/>'
            + F(64, 88, d=9, k=0.6)), 34, 34

def icecream():
    return (f'<path d="M40 64 L64 118 L88 64Z" fill="#E0A830" {s()}/><path d="M46 74 L82 74 M52 88 L76 88 M56 66 L74 102 M72 66 L54 102" stroke="#C08A20" stroke-width="2"/>'
            f'<circle cx="64" cy="52" r="26" fill="#FFB3CF" {s()}/>' + F(64, 54, d=8, k=0.6)), 26, 28

def lemonade():
    return (f'<path d="M34 34 H94 L86 110 H42Z" fill="#FFF3A0" fill-opacity=".95" {s()}/><path d="M38 52 H90" stroke="#fff" stroke-width="3"/>'
            f'<path d="M78 34 L92 10" stroke="#FF7FA8" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="38" cy="38" r="12" fill="#FFE07A" {W(2.6)}/><path d="M38 28 V48 M28 38 H48" stroke="#E0A830" stroke-width="1.6"/>'
            + F(64, 78, d=9, k=0.65)), 30, 32

def salad():
    return (f'<path d="M20 66 H108 Q106 108 64 108 Q22 108 20 66Z" fill="#fff" {s()}/>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="8" fill="#7CD26E" {W(2)} transform="rotate({a} {x} {y})"/>' for x, y, a in [(38, 62, -20), (58, 54, 10), (80, 58, -10), (96, 64, 25)])
            + f'<circle cx="70" cy="62" r="7" fill="#E8554A" {W(2)}/><circle cx="46" cy="60" r="5" fill="#FFD25E" {W(1.6)}/>' + F(64, 86, d=9, k=0.65)), 42, 44

def khachapuri():   # лодочка-хачапури сбоку: тесто-кораблик, сверху сыр и яйцо, лицо на боку
    return (f'<path d="M28 66 Q30 44 64 42 Q98 44 100 66Z" fill="#FFF6DA" {s()}/><circle cx="64" cy="52" r="12" fill="#FFB020" {W(2.6)}/>'
            f'<path d="M6 50 Q14 64 30 66 H98 Q114 64 122 50 Q118 104 64 104 Q10 104 6 50Z" fill="#E0A830" {s()}/>'
            + F(64, 84, d=10, k=0.7)), 40, 44
def croissant():
    return (f'<path d="M14 84 Q20 40 64 40 Q108 40 114 84 Q98 72 86 78 Q78 60 64 60 Q50 60 42 78 Q30 72 14 84Z" fill="#E8A54A" {s()}/>'
            f'<path d="M42 78 Q46 56 64 56 M86 78 Q82 56 64 56" fill="none" stroke="#B87A2A" stroke-width="2.6"/>' + F(64, 48, d=8, k=0.5, blush=False)), 36, 46

def borscht():
    return (f'<path d="M20 64 H108 Q106 106 64 106 Q22 106 20 64Z" fill="#fff" {s()}/><ellipse cx="64" cy="64" rx="44" ry="10" fill="#C0304A" {W(2.6)}/>'
            f'<ellipse cx="72" cy="62" rx="10" ry="4" fill="#fff" {W(1.6)}/><path d="M54 60 l3 -3 M60 66 l3 -3" stroke="#7CD26E" stroke-width="2.4"/>'
            f'<path d="M48 48 Q44 40 50 34 M64 46 Q60 38 66 30 M80 48 Q76 40 82 34" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
            + F(64, 86, d=9, k=0.65)), 30, 44

def ramen():
    return (f'<path d="M18 62 H110 Q108 106 64 106 Q20 106 18 62Z" fill="#E8554A" {s()}/><ellipse cx="64" cy="62" rx="46" ry="10" fill="#FFE9A0" {W(2.6)}/>'
            f'<path d="M80 60 L104 16 M88 62 L112 22" {W(3.4)}/><circle cx="46" cy="60" r="7" fill="#fff" {W(1.6)}/><circle cx="46" cy="60" r="3" fill="#FFB020"/>'
            f'<path d="M28 84 H100" stroke="#fff" stroke-width="3" stroke-dasharray="6 5"/>' + F(64, 90, d=9, k=0.6)), 46, 44

def waffle():
    return (f'<rect x="26" y="34" width="76" height="76" rx="12" fill="#F2B866" {s()}/>'
            + "".join(f'<path d="M{26+i*19} 34 V110 M26 {34+i*19} H102" stroke="#C88A3A" stroke-width="3"/>' for i in (1, 2, 3))
            + f'<circle cx="64" cy="34" r="10" fill="#fff" {W(2.4)}/>' + F(64, 74, d=10, k=0.7)), 22, 38

def nigiri():   # нигири: рис-персонаж, сверху лосось, сбоку ленточка нори
    return (f'<rect x="20" y="62" width="88" height="44" rx="20" fill="#fff" {s()}/>'
            f'<path d="M12 66 Q64 26 116 66 Q64 58 12 66Z" fill="#FF8A5C" {s()}/><path d="M36 52 Q48 46 56 50 M66 44 Q78 40 88 46" stroke="#fff" stroke-width="3" fill="none"/>'
            f'<rect x="24" y="62" width="12" height="44" fill="#2E3A46"/>' + F(70, 86, d=10, k=0.65)), 40, 46

DISH = dict(roll=roll, pizza=pizza, pasta=pasta, plov=plov, teapot=teapot, vareniki=vareniki, khinkali=khinkali,
            cheese=cheese, burger=burger, pancakes=pancakes, cupcake=cupcake, icecream=icecream, lemonade=lemonade,
            salad=salad, khachapuri=khachapuri, croissant=croissant, borscht=borscht, ramen=ramen, waffle=waffle, nigiri=nigiri)
DISH_RU = dict(roll="ролл", pizza="кусочек пиццы", pasta="тарелка пасты", plov="плов", teapot="чайник", vareniki="вареники",
               khinkali="хинкали", cheese="кусок сыра", burger="бургер", pancakes="стопка блинчиков", cupcake="капкейк",
               icecream="мороженое в рожке", lemonade="стакан лимонада", salad="салат в миске", khachapuri="хачапури по-аджарски",
               croissant="круассан", borscht="тарелка борща", ramen="миска рамена", waffle="вафля", nigiri="нигири")

# ---------- аксессуары (крупные, понятные) ----------
def acc(name, top, half):
    cx = 64; t = top
    A = {
        "crown": f'<path d="M{cx-22} {t} L{cx-18} {t-20} L{cx-8} {t-8} L{cx} {t-24} L{cx+8} {t-8} L{cx+18} {t-20} L{cx+22} {t}Z" fill="#FFC93C" {W(3)}/>',
        "party": f'<path d="M{cx-16} {t} L{cx} {t-30} L{cx+16} {t}Z" fill="#A98BF0" {W(3)}/><circle cx="{cx}" cy="{t-31}" r="5" fill="#FFD25E" {W(2)}/><path d="M{cx-10} {t-10} L{cx+8} {t-14}" stroke="#fff" stroke-width="3"/>',
        "bow": f'<path d="M{cx} {t-6} L{cx-20} {t-18} V{t+6}Z M{cx} {t-6} L{cx+20} {t-18} V{t+6}Z" fill="#FF5A8A" {W(2.6)}/><circle cx="{cx}" cy="{t-6}" r="5" fill="#FF5A8A" {W(2.4)}/>',
        "chef": f'<rect x="{cx-16}" y="{t-10}" width="32" height="12" fill="#fff" {W(2.6)}/><path d="M{cx-16} {t-10} Q{cx-28} {t-22} {cx-14} {t-32} Q{cx} {t-44} {cx+14} {t-32} Q{cx+28} {t-22} {cx+16} {t-10}Z" fill="#fff" {W(2.6)}/>',
        "cap": f'<path d="M{cx-20} {t+2} Q{cx-20} {t-22} {cx} {t-22} Q{cx+20} {t-22} {cx+20} {t+2}Z" fill="#E8554A" {W(2.6)}/><path d="M{cx+18} {t} H{cx+38}" {W(5)}/>',
        "beanie": f'<path d="M{cx-22} {t+2} Q{cx-22} {t-24} {cx} {t-24} Q{cx+22} {t-24} {cx+22} {t+2}Z" fill="#3E9BE0" {W(2.6)}/><path d="M{cx-20} {t-8} H{cx+20}" stroke="#fff" stroke-width="4"/><circle cx="{cx}" cy="{t-26}" r="6" fill="#fff" {W(2)}/>',
        "headphones": f'<path d="M{cx-half} {t+24} Q{cx-half} {t-18} {cx} {t-18} Q{cx+half} {t-18} {cx+half} {t+24}" fill="none" {W(5)}/><rect x="{cx-half-8}" y="{t+14}" width="14" height="22" rx="6" fill="#E8554A" {W(2.4)}/><rect x="{cx+half-6}" y="{t+14}" width="14" height="22" rx="6" fill="#E8554A" {W(2.4)}/>',
        "flower": f'<g transform="translate({min(cx+half-6, 100)} {t+2})">' + "".join(f'<circle cx="{8*math.cos(a):.1f}" cy="{8*math.sin(a):.1f}" r="6" fill="#FF7FA8" {W(1.6)}/>' for a in [i * 1.2566 for i in range(5)]) + f'<circle r="5" fill="#FFD25E" {W(1.6)}/></g>',
        "balloon": f'<path d="M{min(cx+half,98)} {t+40} Q104 44 102 40" fill="none" {W(2)}/><ellipse cx="102" cy="26" rx="12" ry="15" fill="#E8554A" {W(2.6)}/>',
        "teddy": f'<g transform="translate({min(cx+half+2, 102)} {t+50})"><circle cx="-9" cy="-14" r="5" fill="#A86F3E" {W(2)}/><circle cx="9" cy="-14" r="5" fill="#A86F3E" {W(2)}/><circle r="13" fill="#C08A5A" {W(2.4)}/>{eye(-4, -1, 0.45)}{eye(4, -1, 0.45)}<ellipse cx="0" cy="5" rx="4" ry="3" fill="#E8C9A0"/></g>',
        "star": f'<path d="M{cx} {t-30} L{cx+6} {t-16} L{cx+21} {t-15} L{cx+9} {t-6} L{cx+13} {t+8} L{cx} {t} L{cx-13} {t+8} L{cx-9} {t-6} L{cx-21} {t-15} L{cx-6} {t-16}Z" fill="#FFD25E" {W(2.6)}/>',
        "heart": f'<path d="M{cx} {t-4} q-10 -16 -20 -6 q-8 10 20 24 q28 -14 20 -24 q-10 -10 -20 6Z" fill="#FF5A6A" {W(2.4)}/>',
        "sprout": f'<path d="M{cx} {t+2} V{t-14}" stroke="#5CB04F" stroke-width="4"/><path d="M{cx} {t-12} Q{cx-18} {t-26} {cx-22} {t-10} Q{cx-8} {t-6} {cx} {t-12}Z M{cx} {t-14} Q{cx+16} {t-30} {cx+22} {t-14} Q{cx+8} {t-8} {cx} {t-14}Z" fill="#7CD26E" {W(2.2)}/>',
        "tiara": f'<path d="M{cx-20} {t} Q{cx} {t-22} {cx+20} {t}" fill="none" stroke="#C0C4D0" stroke-width="5"/><circle cx="{cx}" cy="{t-14}" r="5" fill="#9ED3FF" {W(2)}/><circle cx="{cx-12}" cy="{t-8}" r="3" fill="#FF7FA8"/><circle cx="{cx+12}" cy="{t-8}" r="3" fill="#FF7FA8"/>',
        "cherry": f'<path d="M{cx} {t-6} Q{cx+4} {t-22} {cx+14} {t-26}" fill="none" stroke="#5CB04F" stroke-width="3"/><circle cx="{cx}" cy="{t-4}" r="9" fill="#E8304A" {W(2.4)}/>',
        "umbrella": f'<path d="M{cx+half-30} {t-6} Q{cx+half-6} {t-34} {cx+half+18} {t-6}Z" fill="#5CB7F2" {W(2.6)}/><path d="M{cx+half-6} {t-6} V{t+30} Q{cx+half-6} {t+38} {cx+half-14} {t+34}" fill="none" {W(3)}/>',
        "bowtie": f'<path d="M{cx} {t+half+36} L{cx-18} {t+half+26} V{t+half+46}Z M{cx} {t+half+36} L{cx+18} {t+half+26} V{t+half+46}Z" fill="#3B3355"/>',
        "rainbow": "".join(f'<path d="M{cx-36+i*6} {t+4} Q{cx} {t-38+i*6} {cx+36-i*6} {t+4}" fill="none" stroke="{c}" stroke-width="5"/>' for i, c in enumerate(["#E8554A", "#FFC93C", "#7CD26E", "#3E9BE0"])),
        "wand": f'<path d="M{min(cx+half+8,110)} {t+44} L{min(cx+half-6,96)} {t+8}" stroke="#A86F3E" stroke-width="4" stroke-linecap="round"/><path d="M{min(cx+half-6,96)} {t-10} l4 9 l10 1 l-8 6 l3 10 l-9 -5 l-9 5 l3 -10 l-8 -6 l10 -1Z" fill="#FFD25E" {W(2.2)}/>',
        "bunnyears": f'<ellipse cx="{cx-12}" cy="{t-18}" rx="7" ry="18" fill="#fff" {W(2.6)}/><ellipse cx="{cx+12}" cy="{t-18}" rx="7" ry="18" fill="#fff" {W(2.6)}/><ellipse cx="{cx-12}" cy="{t-18}" rx="3" ry="11" fill="#FF7FA8"/><ellipse cx="{cx+12}" cy="{t-18}" rx="3" ry="11" fill="#FF7FA8"/>',
        "graduate": f'<path d="M{cx-26} {t-12} L{cx} {t-24} L{cx+26} {t-12} L{cx} {t}Z" fill="#3B3355" {W(2.4)}/><path d="M{cx-14} {t-6} V{t+2} H{cx+14} V{t-6}" fill="#3B3355" {W(2.4)}/><path d="M{cx+24} {t-12} V{t+6}" stroke="#FFC93C" stroke-width="3"/><circle cx="{cx+24}" cy="{t+8}" r="3" fill="#FFC93C"/>',
        "cowboy": f'<ellipse cx="{cx}" cy="{t}" rx="32" ry="7" fill="#C08A5A" {W(2.6)}/><path d="M{cx-16} {t-2} Q{cx-16} {t-26} {cx} {t-20} Q{cx+16} {t-26} {cx+16} {t-2}Z" fill="#C08A5A" {W(2.6)}/>',
        "wreath": "".join(f'<circle cx="{cx+dx}" cy="{t-4+abs(dx)//4}" r="6" fill="{c}" {W(1.6)}/>' for dx, c in [(-24, "#FF7FA8"), (-12, "#FFD25E"), (0, "#9ED3FF"), (12, "#FF7FA8"), (24, "#FFD25E")]),
        "propeller": f'<path d="M{cx-18} {t+2} Q{cx-18} {t-18} {cx} {t-18} Q{cx+18} {t-18} {cx+18} {t+2}Z" fill="#7CD26E" {W(2.6)}/><path d="M{cx} {t-18} V{t-26}" {W(3)}/><ellipse cx="{cx-10}" cy="{t-28}" rx="10" ry="4" fill="#E8554A" {W(2)}/><ellipse cx="{cx+10}" cy="{t-28}" rx="10" ry="4" fill="#3E9BE0" {W(2)}/>',
        "santa": f'<path d="M{cx-22} {t} Q{cx} {t-34} {cx+26} {t-22} L{cx+22} {t}Z" fill="#E8304A" {W(2.6)}/><rect x="{cx-24}" y="{t-6}" width="48" height="10" rx="5" fill="#fff" {W(2.4)}/><circle cx="{cx+28}" cy="{t-22}" r="6" fill="#fff" {W(2.2)}/>',
        "pirate": f'<path d="M{cx-26} {t+2} Q{cx} {t-30} {cx+26} {t+2} Q{cx} {t-6} {cx-26} {t+2}Z" fill="#3B3355" {W(2.4)}/><circle cx="{cx}" cy="{t-10}" r="4" fill="#fff"/>',
    }
    return A[name]


ACC = ["crown", "party", "bow", "chef", "cap", "beanie", "headphones", "flower", "balloon", "teddy", "star", "heart",
       "sprout", "tiara", "cherry", "umbrella", "rainbow", "wand", "bunnyears", "graduate", "cowboy", "wreath", "propeller", "santa", "pirate"]
ACC_RU = dict(crown="в короне", party="в праздничном колпачке", bow="с бантом", chef="в поварском колпаке", cap="в кепке",
              beanie="в шапке с помпоном", headphones="в наушниках", flower="с цветком", balloon="с воздушным шариком",
              teddy="с плюшевым мишкой", star="со звездой", heart="с сердечком", sprout="с росточком на макушке",
              tiara="в диадеме", cherry="с вишенкой на макушке", umbrella="под зонтиком", rainbow="под радугой",
              wand="с волшебной палочкой", bunnyears="с заячьими ушками", graduate="в шапке выпускника", cowboy="в ковбойской шляпе", wreath="в цветочном венке", propeller="в кепке с пропеллером", santa="в новогоднем колпаке", pirate="в пиратской треуголке")
BGS = ["blue", "green", "orange", "pink", "purple", "yellow", "teal", "sky"]

CHAIN = [("yakitoriya", "roll"), ("niyama", "nigiri"), ("upsushi", "ramen"), ("hatimaki", "ramen"), ("chaihona", "teapot"),
         ("uryuk", "plov"), ("tapchan", "plov"), ("syrovarnya", "cheese"), ("ilpatio", "pizza"), ("bocconcino", "pizza"),
         ("pronto", "burger"), ("gambrinus", "burger"), ("korchma", "borscht"), ("osteria", "pasta"), ("mimi", "pancakes"),
         ("varenichnaya", "vareniki"), ("botanika", "salad"), ("dyushes", "lemonade")]
CUISINE = [(r"хинкал|грузин|tiflis|тифлис|kazbek|казбек|imereti|имерет|ketsi|кеци|marani|марани|qartuli|satsebeli|сацебели|mariko|batono|джонджол|dzhondzholi|khachapuri|хачапури|alubali|алубали|tramplin|gruzinskiy", "khachapuri"),
           (r"суши|ролл|sushi|яп|japan|niyama", "roll"), (r"пицц|pizza|ital|итал|trattoria|траттор|pasta|паст|osteria|semplice|pioppo|largo|caramelle|casa|nonna|vesna", "pasta"),
           (r"узбек|чайхон|плов|tapchan|топчан|firdusi|фирдуси|baku|баку|azerbaijan|азерб|meyhana|мейхана|elardzhi|kinza|кинза", "plov"),
           (r"пекин|китай|peking|utka", "ramen")]
KEEP = re.compile(r"крендел|печенье с предсказ|тако|онигири|голубцы|наггетс|луковые кольца|лазань|чурро|тирамису|брауни|чебурек|корн-дог|"
                  r"трдельник|сэндвич с мороженым|банана-сплит|вафельная трубочка|паэлья|рёбрышки|ватрушк|кулич|бенто-торт|козинаки|"
                  r"мармеладный мишка|карамельная трость|коробка конфет|желе на тарелке|крем-карамель|трюфель|глазированный сырок|"
                  r"маршмеллоу|самовар|чак-чак|сулугуни|гриссини|пачка чипсов|детский стульчик|детская тарелка|тайяки", re.I)


def plan():
    places = [p for p in json.load(open(os.path.join(ROOT, "places.json")))["places"] if "food" in p["cats"]]
    subj = {}
    for l in open(os.path.join(OUT, "subjects.txt")):
        if " — " in l: k, v = l.rstrip("\n").split(" — ", 1); subj[k] = v
    todo = []
    for p in places:
        pid = p["id"]
        if pid not in subj: continue                       # встроенные в приложение — не трогаем
        chain = next((d for k, d in CHAIN if k in pid), None)
        if not chain and KEEP.search(subj[pid]): continue  # понятная еда — оставить
        dish = chain or next((d for rx, d in CUISINE if re.search(rx, pid + " " + p["name"], re.I)), None)
        todo.append([pid, p["name"], dish])
    # без кухни — по кругу понятных десертов/блюд
    pool = ["cupcake", "pancakes", "waffle", "icecream", "croissant", "burger", "khinkali", "lemonade", "salad", "vareniki"]
    i = 0
    for t in todo:
        if not t[2]: t[2] = pool[i % len(pool)]; i += 1
    # аксессуар: уникальная пара блюдо+аксессуар
    used = {}
    ALT = dict(pasta="pizza", pizza="pasta", roll="nigiri", nigiri="roll", plov="teapot", teapot="plov", ramen="roll")
    for t in todo:
        if used.get(t[2], 0) >= len(ACC) and t[2] in ALT: t[2] = ALT[t[2]]
        n = used.get(t[2], 0); used[t[2]] = n + 1
        t.append(ACC[n % len(ACC)]); t.append(BGS[(n * 3 + len(t[2])) % len(BGS)])
        if n >= len(ACC): print("!! повтор пары", t)
    return todo


if __name__ == "__main__":
    todo = plan()
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for pid, name, dish, a, bg in todo:
        body, top, half = DISH[dish]()
        svgtxt = svg(bg, body + acc(a, top, half))
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(svgtxt)
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
        txt += f"{pid} — {DISH_RU[dish]} {ACC_RU[a]}\n"
    open(reg, "w").write(txt)
    from collections import Counter
    print(len(todo), Counter(t[2] for t in todo))
    json.dump([t[0] for t in todo], open("/tmp/claude-0/cafe_ids.json", "w"))
