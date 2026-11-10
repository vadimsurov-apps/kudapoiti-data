"""Кафе v2 (07.11): по уроку бассейнов — не «одно блюдо + разные шапки», а СЦЕНЫ в детской комнате кафе.
Герой — готовое блюдо-персонаж (по кухне заведения), сцена — что происходит в детской: сухой бассейн, горка,
детский стульчик, качели, лошадка-качалка, «ложечка-самолётик», день рождения, мольберт, кукольный театр, фокусник…
Пара «сцена + блюдо» не повторяется; у сцены 2 раскладки (позиция/размер/зеркало) и разные фоны."""
import json, math, os, re, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
import icons_cafes_1106 as C
W = lambda w: s(f'stroke-width="{w}"')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
F = lambda x, y, d=8, k=0.7, **kw: face(x, y, d=d, k=k, **kw)


# ---- дополнительные блюда (центр 64,64) ----
def donut():
    return (f'<circle cx="64" cy="66" r="40" fill="#E8A54A" {s()}/><path d="M28 60 Q30 30 64 28 Q98 30 100 60 Q96 74 84 66 Q74 80 64 70 Q52 80 44 66 Q32 74 28 60Z" fill="#FF8FB1" {W(2.6)}/>'
            + "".join(f'<rect x="{x}" y="{y}" width="8" height="3" rx="1.5" fill="{c}" transform="rotate({a} {x} {y})"/>' for x, y, a, c in [(44, 44, 30, "#fff"), (78, 40, -20, "#FFD25E"), (60, 34, 70, "#7CD26E"), (86, 56, 40, "#9ED3FF")])
            + f'<ellipse cx="64" cy="70" rx="12" ry="8" fill="#FBEEE5" {W(2.4)}/>' + F(64, 88, d=10, k=0.6)), 30, 40


def cakeslice():
    return (f'<path d="M20 60 L108 40 V96 L20 110Z" fill="#FFE3A3" {s()}/><path d="M20 60 L108 40 L92 28 L16 50Z" fill="#FFB3CF" {s()}/>'
            f'<path d="M20 82 L108 66" stroke="#FF8FB1" stroke-width="6"/><circle cx="60" cy="34" r="8" fill="#E8304A" {W(2.2)}/>'
            + F(64, 88, d=9, k=0.6)), 30, 40


def cocoa():
    return (f'<path d="M98 52 Q118 52 116 70 Q114 86 96 84" fill="none" {W(6)}/>'
            f'<path d="M28 44 H100 L94 104 Q92 112 84 112 H44 Q36 112 34 104Z" fill="#FF8A5C" {s()}/>'
            f'<ellipse cx="64" cy="44" rx="36" ry="9" fill="#8A5530" {W(2.6)}/>'
            + "".join(f'<rect x="{x}" y="{y}" width="12" height="10" rx="4" fill="#fff" {W(1.8)}/>' for x, y in [(44, 34), (60, 30), (74, 36)])
            + F(64, 78, d=10, k=0.7)), 28, 36


def hotdog():
    return (f'<path d="M12 70 Q12 50 34 54 H94 Q116 50 116 70 Q116 92 94 88 H34 Q12 92 12 70Z" fill="#E8A54A" {s()}/>'
            f'<rect x="20" y="58" width="88" height="18" rx="9" fill="#C0503A" {s()}/>'
            f'<path d="M28 62 Q36 56 44 62 T60 62 T76 62 T92 62 T104 62" fill="none" stroke="#FFD25E" stroke-width="4"/>' + F(64, 80, d=10, k=0.6)), 52, 46


def cookie():
    return (f'<circle cx="64" cy="64" r="44" fill="#E0A870" {s()}/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#6B3E26"/>' for x, y, r in [(40, 44, 5), (86, 46, 6), (34, 78, 4), (92, 84, 5), (62, 34, 4), (70, 98, 4)])
            + F(64, 66, d=10, k=0.75)), 22, 44


DISH = dict(C.DISH, donut=donut, cakeslice=cakeslice, cocoa=cocoa, hotdog=hotdog, cookie=cookie)
DISH_RU = dict(C.DISH_RU, donut="пончик", cakeslice="кусочек торта", cocoa="кружка какао", hotdog="хот-дог", cookie="печенька")


def put(d, x, y, k=0.6, flip=False, rot=0):
    body = DISH[d]()[0]
    sx = -k if flip else k
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sx} {k}) translate(-64 -64)">{body}</g>'


def balls(y0=96):
    cols = ["#E8554A", "#FFC93C", "#3E9BE0", "#7CD26E", "#A98BF0", "#FF8FB1"]
    return "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{cols[(i*5) % 6]}" {W(2)}/>' for i, (x, y) in enumerate(
        [(x, y0 + (x * 7 % 9)) for x in range(4, 128, 15)] + [(x + 7, y0 + 14 + (x * 3 % 7)) for x in range(0, 128, 15)] + [(x, y0 + 28) for x in range(4, 128, 15)]))


def bunting(y=14):
    cols = ["#E8554A", "#FFC93C", "#3E9BE0", "#7CD26E", "#FF8FB1"]
    return f'<path d="M0 {y} Q64 {y+16} 128 {y}" fill="none" {W(2)}/>' + "".join(
        f'<path d="M{x-6} {y+5+abs(64-x)/-12+8:.0f} L{x+6} {y+5+abs(64-x)/-12+8:.0f} L{x} {y+19+abs(64-x)/-12+8:.0f}Z" fill="{cols[i % 5]}" {W(1.6)}/>' for i, x in enumerate(range(16, 128, 16)))


# ---------- сцены детской комнаты ----------
def S_ballpit(d, v):
    return put(d, 64 if v == 0 else 50, 62, 0.62, flip=bool(v)) + balls(92) + f'<rect x="0" y="0" width="0" height="0"/>'


def S_slide(d, v):
    sl = (f'<path d="M20 36 L20 120" {W(6)}/><path d="M20 36 H42 L112 112 H94 L34 52 H20Z" fill="#FFC93C" {s()}/>'
          + "".join(f'<path d="M14 {y} H26" {W(4)}/>' for y in (56, 76, 96)))
    return sl + (put(d, 42, 26, 0.55) if v == 0 else put(d, 86, 82, 0.55, rot=40))


def S_highchair(d, v):
    ch = (f'<path d="M36 128 L46 84 M92 128 L82 84" {W(6)}/><path d="M38 50 Q38 30 64 30 Q90 30 90 50 V84 H38Z" fill="#FFB3CF" {s()}/>'
          f'<rect x="24" y="78" width="80" height="10" rx="5" fill="#fff" {W(2.6)}/>')
    return ch + put(d, 64, 54, 0.56, flip=bool(v))


def S_birthday(d, v):
    return (bunting() + f'<rect x="16" y="100" width="96" height="10" rx="5" fill="#fff" {W(2.4)}/>'
            + put(d, 64, 70, 0.58, flip=bool(v))
            + f'<rect x="{60 if v == 0 else 86}" y="22" width="7" height="18" rx="2" fill="#7CD26E" {W(2)}/><path d="M{63.5 if v == 0 else 89.5} 22 q-5 -8 0 -12 q5 4 0 12Z" fill="#FFC93C" {W(1.6)}/>')


def S_horse(d, v):
    horse = (f'<path d="M14 116 Q64 92 114 116" fill="none" stroke="#A86F3E" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M28 104 L36 84 M96 104 L88 84" {W(5)}/>'
             f'<path d="M30 70 Q30 92 60 92 H92 Q102 92 100 76 L104 48 Q108 36 98 34 L88 32 Q80 34 84 46 L84 66 H48 Q36 60 30 70Z" fill="#fff" {s()}/>'
             f'<path d="M88 32 Q96 22 102 34" fill="#E8554A" {W(2.4)}/><circle cx="96" cy="42" r="2.6" fill="{O}"/><path d="M30 70 Q18 72 20 88" fill="none" stroke="#E8554A" stroke-width="5" stroke-linecap="round"/>')
    return horse + put(d, 62, 44, 0.55)


def S_swing(d, v):
    return (f'<path d="M0 10 H128" {W(6)}/><path d="M{36 if v == 0 else 46} 10 L{30 if v == 0 else 58} 96 M{92 if v == 0 else 102} 10 L{86 if v == 0 else 112} 96" {W(3)}/>'
            f'<rect x="{24 if v == 0 else 52}" y="94" width="{68}" height="9" rx="4" fill="#E8554A" {W(2.4)}/>'
            + put(d, 58 if v == 0 else 84, 70, 0.48, rot=-6 if v == 0 else 8)
            + f'<path d="M12 70 q8 4 4 12 M118 50 q-8 4 -4 12" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')


def S_spoonplane(d, v):
    plane = (f'<path d="M14 92 Q40 86 64 82" stroke="{O}" stroke-width="10" stroke-linecap="round"/><path d="M14 92 Q40 86 64 82" stroke="#C0C4D0" stroke-width="6" stroke-linecap="round"/>'
             f'<ellipse cx="82" cy="78" rx="24" ry="13" fill="#C0C4D0" {s()}/>'
             f'<path d="M30 80 L40 64 L50 86Z M26 96 L18 106 L34 100Z" fill="#E8554A" {W(2.2)}/>')
    clouds = f'<path d="M86 22 q4 -10 14 -6 q8 -6 14 2 q8 2 4 10 H88 q-6 0 -2 -6Z" fill="#fff" {W(2)}/>' if v == 0 else f'<path d="M10 30 q4 -10 14 -6 q8 -6 14 2 q8 2 4 10 H12 q-6 0 -2 -6Z" fill="#fff" {W(2)}/>'
    return clouds + plane + put(d, 82, 54, 0.46) + f'<path d="M4 70 H20 M0 80 H14" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'


def S_balloons(d, v):
    cols = [("#E8554A", 34, 22), ("#FFC93C", 64, 12), ("#3E9BE0", 94, 24)]
    return ("".join(f'<path d="M{x} {y+14} Q{(x+64)/2} {y+40} 64 {64}" fill="none" {W(1.8)}/>' for c, x, y in cols)
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="15" fill="{c}" {W(2.4)}/><path d="M{x-4} {y-7} q3 -4 7 -3" fill="none" stroke="#fff" stroke-width="2.4"/>' for c, x, y in cols)
            + put(d, 64, 88, 0.56, flip=bool(v)))


def S_teddy(d, v):
    t = (f'<g transform="translate({30 if v == 0 else 98} 78)"><circle cx="-12" cy="-26" r="8" fill="#C98A5E" {W(2.2)}/><circle cx="12" cy="-26" r="8" fill="#C98A5E" {W(2.2)}/>'
         f'<ellipse cx="0" cy="12" rx="18" ry="16" fill="#C98A5E" {s()}/><circle cx="0" cy="-12" r="16" fill="#C98A5E" {s()}/>'
         f'<ellipse cx="0" cy="-6" rx="7" ry="5" fill="#F2D3AE"/>' + eye(-6, -15, 0.55) + eye(6, -15, 0.55) + f'<ellipse cx="0" cy="-8" rx="2.4" ry="1.8" fill="{O}"/></g>')
    return (f'<rect x="0" y="100" width="128" height="28" fill="#FFE3A3" {W(2.4)}/>' + t + put(d, 84 if v == 0 else 44, 72, 0.5))


def S_tray(d, v):
    juice = (f'<g transform="translate({96 if v == 0 else 30} 70)"><rect x="-12" y="-18" width="24" height="34" rx="4" fill="#7CD26E" {s()}/>'
             f'<path d="M4 -18 L10 -34 L16 -34" fill="none" stroke="{O}" stroke-width="5" stroke-linecap="round"/><path d="M4 -18 L10 -34 L16 -34" fill="none" stroke="#FF7FA8" stroke-width="2.6" stroke-linecap="round"/>'
             f'<circle cx="0" cy="0" r="6" fill="#FFC93C" {W(1.6)}/></g>')
    return (f'<path d="M6 92 H122 L114 108 H14Z" fill="#E8554A" {s()}/>' + juice + put(d, 50 if v == 0 else 80, 62, 0.5))


def S_easel(d, v):
    e = (f'<path d="M78 120 L90 28 L102 120 M84 96 H96" {W(4)}/><rect x="70" y="20" width="44" height="52" rx="3" fill="#fff" {s()}/>'
         f'<path d="M80 56 Q92 30 104 56" fill="none" stroke="#E8554A" stroke-width="4"/><circle cx="92" cy="40" r="5" fill="#FFC93C"/>'
         f'<path d="M40 50 L58 34" stroke="#A86F3E" stroke-width="4" stroke-linecap="round"/><path d="M58 34 L64 28" stroke="#3E9BE0" stroke-width="7" stroke-linecap="round"/>')
    return e + put(d, 40, 82, 0.5)


def S_teepee(d, v):
    return (f'<path d="M64 8 L18 116 H110Z" fill="#FFE3A3" {s()}/><path d="M50 8 L64 26 L78 8" fill="none" {W(3)}/>'
            f'<path d="M64 46 L40 116 H88Z" fill="#8A5530" {W(2.4)}/>'
            + "".join(f'<path d="M{64-dx} {y} L{64+dx} {y}" stroke="{c}" stroke-width="4"/>' for dx, y, c in [(18, 40, "#E8554A"), (26, 58, "#3E9BE0")])
            + put(d, 64, 92, 0.46, flip=bool(v)))


def S_train(d, v):
    return (f'<path d="M0 112 H128" stroke="#A86F3E" stroke-width="5"/>'
            f'<rect x="{8 if v == 0 else 66}" y="62" width="54" height="40" rx="6" fill="#E8554A" {s()}/><rect x="{16 if v == 0 else 74}" y="46" width="22" height="18" fill="#E8554A" {W(2.4)}/>'
            f'<rect x="{66 if v == 0 else 8}" y="80" width="54" height="22" rx="4" fill="#3E9BE0" {s()}/>'
            + "".join(f'<circle cx="{x}" cy="106" r="7" fill="#3B3355" {W(2)}/>' for x in (22, 48, 80, 106))
            + put(d, 93 if v == 0 else 35, 60, 0.48) + f'<path d="M{27 if v == 0 else 85} 44 q-4 -10 4 -16 q-6 -8 2 -14" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>')


def S_trampoline(d, v):
    return (f'<ellipse cx="64" cy="104" rx="48" ry="11" fill="#5CB7F2" {s()}/><path d="M22 106 L28 122 M106 106 L100 122" {W(5)}/>'
            + put(d, 64, 52, 0.6, rot=-10 if v else 10) + f'<path d="M30 70 q-6 8 0 16 M98 70 q6 8 0 16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')


def S_magichat(d, v):
    return (f'<ellipse cx="64" cy="112" rx="40" ry="8" fill="#3B3355" {s()}/><path d="M38 112 V78 H90 V112Z" fill="#3B3355" {s()}/>'
            f'<rect x="38" y="96" width="52" height="8" fill="#E8554A"/>'
            + put(d, 64, 50, 0.56) + sparkle(22, 30, 8) + sparkle(106, 22, 7) + sparkle(110, 70, 5))


def S_puppet(d, v):
    return (f'<rect x="10" y="64" width="108" height="56" fill="#E8554A" {s()}/><path d="M10 14 Q38 40 34 64 H10Z M118 14 Q90 40 94 64 H118Z" fill="#A83A6A" {s()}/>'
            f'<path d="M10 10 H118 V22 Q64 30 10 22Z" fill="#FFC93C" {s()}/>' + put(d, 64, 52, 0.54, flip=bool(v)))


def S_picnic(d, v):
    cloth = "".join(f'<rect x="{x}" y="{y}" width="16" height="12" fill="{"#E8554A" if (x//16 + y//12) % 2 else "#fff"}"/>' for x in range(0, 128, 16) for y in range(84, 128, 12))
    return (f'<path d="M0 84 H128 V128 H0Z" fill="#fff"/>' + cloth + f'<path d="M0 84 H128" {W(2.6)}/>'
            + put(d, 64, 60, 0.6, flip=bool(v)) + f'<path d="M{18 if v == 0 else 96} 40 l3 6 l6 1 l-5 4 l1 6 l-5 -3 l-5 3 l1 -6 l-5 -4 l6 -1Z" fill="#FFC93C" {W(1.4)}/>')


def S_hearts(d, v):
    return (put(d, 64, 74, 0.66) + "".join(f'<path d="M{x} {y} q-6 -9 -12 -3 q-4 6 12 14 q16 -8 12 -14 q-6 -6 -12 3Z" fill="#FF5A6A" {W(1.8)}/>' for x, y in ([(40, 20), (82, 10), (100, 30)] if v == 0 else [(28, 30), (64, 8), (96, 22)])))


def S_twins(d, v):
    return put(d, 46, 66, 0.6) + put(d, 98, 86, 0.32, flip=True) + f'<path d="M78 34 q-5 -8 -10 -2 q-4 6 10 14 q14 -8 10 -14 q-5 -6 -10 2Z" fill="#FF5A6A" {W(1.8)}/>'


def S_chefkid(d, v):
    kid = (f'<g transform="translate({36 if v == 0 else 92} 74)"><path d="M-14 22 Q-16 46 0 46 Q16 46 14 22Z" fill="#fff" {s()}/>'
           f'<circle r="16" fill="#FFD9B8" {s()}/>' + F(0, 2, d=6, k=0.45)
           + f'<rect x="-13" y="-22" width="26" height="9" fill="#fff" {W(2.2)}/><path d="M-13 -22 Q-24 -30 -12 -40 Q0 -50 12 -40 Q24 -30 13 -22Z" fill="#fff" {W(2.2)}/></g>')
    return kid + put(d, 92 if v == 0 else 38, 70, 0.48)


def S_bib(d, v):
    return (f'<rect x="0" y="96" width="128" height="32" fill="#FFE3A3" {W(2.4)}/>'
            + f'<path d="M{18 if v == 0 else 104} 56 V96 M{14 if v == 0 else 100} 56 V68 M{22 if v == 0 else 108} 56 V68 M{14 if v == 0 else 100} 68 Q{18 if v == 0 else 104} 74 {22 if v == 0 else 108} 68" fill="none" {W(3)}/>'
            + put(d, 66, 62, 0.6)
            + f'<path d="M52 82 L80 82 L66 102Z" fill="#fff" {W(2.4)}/><circle cx="66" cy="88" r="3" fill="#FF8FB1"/>')


def S_carousel(d, v):
    return (f'<path d="M14 40 L64 12 L114 40Z" fill="#E8554A" {s()}/><path d="M14 40 Q26 48 39 40 Q51 48 64 40 Q77 48 89 40 Q102 48 114 40" fill="#fff" {W(2)}/>'
            f'<path d="M64 12 V4" {W(3)}/><circle cx="64" cy="4" r="3" fill="#FFC93C"/>'
            f'<path d="M30 46 V110 M98 46 V110" stroke="#FFC93C" stroke-width="5"/><ellipse cx="64" cy="114" rx="54" ry="9" fill="#3E9BE0" {s()}/>'
            + put(d, 64, 78, 0.52, flip=bool(v)))


def S_bubbles(d, v):
    return (put(d, 58 if v == 0 else 70, 72, 0.62) + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".35" stroke="#fff" stroke-width="2.4"/>'
                                                          f'<path d="M{x-r*0.5} {y-r*0.3} q{r*0.2} {-r*0.4} {r*0.5} {-r*0.5}" fill="none" stroke="#fff" stroke-width="2"/>'
                                                          for x, y, r in [(20, 30, 10), (104, 22, 13), (110, 70, 8), (16, 84, 7), (84, 104, 6)]))


def S_drum(d, v):
    return (f'<ellipse cx="64" cy="98" rx="38" ry="10" fill="#fff" {s()}/><path d="M26 98 V118 Q64 132 102 118 V98" fill="#E8554A" {s()}/>'
            f'<path d="M30 104 L44 122 L58 106 L72 124 L86 106 L98 120" fill="none" stroke="#FFC93C" stroke-width="3"/>'
            + put(d, 64, 54, 0.5) + f'<path d="M22 50 L44 86 M106 50 L84 86" stroke="#A86F3E" stroke-width="5" stroke-linecap="round"/>'
            + f'<text x="{14 if v == 0 else 100}" y="30" font-family="Arial" font-weight="700" font-size="20" fill="#fff" stroke="{O}" stroke-width="1.2">♪</text>')


def S_car(d, v):
    return (f'<path d="M10 96 Q12 70 34 68 L50 52 H86 L102 68 Q118 70 118 96Z" fill="#7CD26E" {s()}/>'
            f'<circle cx="34" cy="100" r="11" fill="#3B3355" {W(2.4)}/><circle cx="94" cy="100" r="11" fill="#3B3355" {W(2.4)}/>'
            f'<circle cx="34" cy="100" r="4" fill="#C0C4D0"/><circle cx="94" cy="100" r="4" fill="#C0C4D0"/>'
            + put(d, 66, 44, 0.5) + f'<path d="M100 66 L112 62" {W(3)}/>')


def S_crayons(d, v):
    cr = "".join(f'<g transform="translate({x} {y}) rotate({a})"><rect x="-4" y="-22" width="8" height="34" fill="{c}" {W(2)}/><path d="M-4 -22 L0 -30 L4 -22Z" fill="{c}" {W(1.6)}/></g>'
                 for x, y, a, c in [(20, 104, -30, "#E8554A"), (36, 112, -10, "#3E9BE0"), (96, 110, 20, "#7CD26E"), (110, 100, 34, "#FFC93C")])
    return (f'<rect x="14" y="82" width="100" height="40" rx="4" fill="#fff" {s()}/><path d="M24 104 Q40 88 56 104 T88 104" fill="none" stroke="#FF8FB1" stroke-width="4"/>'
            + put(d, 64, 48, 0.55, flip=bool(v)) + cr)


def S_photo(d, v):
    return (f'<rect x="18" y="18" width="92" height="92" rx="8" fill="#fff" {s()}/><rect x="26" y="26" width="76" height="66" fill="#CFEFFF"/>'
            + put(d, 64, 62, 0.5, flip=bool(v)) + sparkle(98, 30, 9, "#FFD25E") + f'<path d="M48 100 H80" stroke="#FF8FB1" stroke-width="4"/>')


SCENES = dict(ballpit=S_ballpit, slide=S_slide, highchair=S_highchair, birthday=S_birthday, horse=S_horse, swing=S_swing,
              spoonplane=S_spoonplane, balloons=S_balloons, teddy=S_teddy, tray=S_tray, easel=S_easel, teepee=S_teepee,
              train=S_train, trampoline=S_trampoline, magichat=S_magichat, puppet=S_puppet, picnic=S_picnic, hearts=S_hearts,
              twins=S_twins, chefkid=S_chefkid, bib=S_bib, carousel=S_carousel, bubbles=S_bubbles, drum=S_drum, car=S_car,
              crayons=S_crayons, photo=S_photo)
SCENE_RU = dict(ballpit="выглядывает из сухого бассейна с шариками", slide="катается с детской горки", highchair="сидит в детском стульчике",
                birthday="на дне рождения со свечкой и флажками", horse="скачет на лошадке-качалке", swing="качается на качелях",
                spoonplane="летит на ложечке-самолётике", balloons="улетает на воздушных шариках", teddy="обедает с плюшевым мишкой",
                tray="на подносе детского меню с соком", easel="рисует у мольберта", teepee="прячется в детском вигваме",
                train="едет в вагончике игрушечного паровоза", trampoline="прыгает на батутике", magichat="появляется из шляпы фокусника",
                puppet="выступает в кукольном театре", picnic="на клетчатой скатерти", hearts="дымится сердечками",
                twins="мама и малыш рядом", chefkid="у маленького повара в колпаке", bib="за столом в салфетке-слюнявчике",
                carousel="катается на карусели", bubbles="среди мыльных пузырей", drum="играет на барабане на детском празднике",
                car="едет на детской машинке", crayons="с карандашами и раскраской", photo="в фоторамке со вспышкой")
BGS = ["sky", "teal", "yellow", "pink", "purple", "orange", "green", "blue"]
CUIS = [(r"хинкал|грузин|tiflis|тифлис|kazbek|казбек|imereti|имерет|ketsi|кеци|marani|марани|qartuli|satsebeli|сацебели|mariko|batono|джонджол|dzhondzholi|khachapuri|хачапури|alubali|алубали|tramplin|gruzinskiy|грузия|georg", ["khachapuri", "khinkali", "cheese"]),
        (r"суши|ролл|sushi|якитор|yakitor|niyama|нияма|hatimaki|upsushi|тануки|tanuki|japan|япон|wok|вок|ramen|рамен|пекин|китай|peking", ["roll", "nigiri", "ramen"]),
        (r"пицц|pizza|ital|итал|trattoria|траттор|pasta|паст|osteria|остери|semplice|pioppo|largo|caramelle|casa|nonna|bocconcino|patio|патио", ["pizza", "pasta", "cheese"]),
        (r"узбек|чайхон|chaihona|плов|tapchan|топчан|урюк|uryuk|firdusi|фирдуси|baku|баку|azerb|азерб|meyhana|мейхана|kinza|кинза|самарканд|бухар|восток", ["plov", "teapot", "cocoa"]),
        (r"корчма|korchma|варенич|varenich|украин|русск|блин|mimi|теремок|пельмен|шоколадниц|anderson|андерсон|кофе|coffee|cafe|кондитер|пекарн|bakery", ["pancakes", "borscht", "vareniki", "croissant", "cakeslice", "cocoa", "donut", "cookie", "cupcake", "waffle"]),
        (r"бургер|burger|гриль|grill|steak|стейк|beer|пиво|gambrinus|pronto|american|дайнер|diner", ["burger", "hotdog", "lemonade"])]
ALLD = list(DISH)


def plan():
    places = [p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"] if "food" in p["cats"]]
    bundled = set(json.load(open(os.path.join(ROOT, "tools", "bundled_icons.json"))))
    rnd = random.Random(11)
    used, sn, dn, todo = set(), {}, {}, []
    for i, p in enumerate(places):
        pid = p["id"]
        if pid in bundled:
            continue
        pref = next((ds for rx, ds in CUIS if re.search(rx, pid + " " + p["name"], re.I)), None)
        cands = []
        for sc in rnd.sample(list(SCENES), len(SCENES)):
            for d in rnd.sample(ALLD, len(ALLD)):
                if (sc, d) in used: continue
                cost = sn.get(sc, 0) * 3 + dn.get(d, 0) * 2 - (8 if pref and d in pref else 0)
                cands.append((cost, sc, d))
        cost, sc, d = min(cands)
        used.add((sc, d)); sn[sc] = sn.get(sc, 0) + 1; dn[d] = dn.get(d, 0) + 1
        todo.append(dict(id=pid, scene=sc, dish=d, v=(sn[sc] - 1) % 2, bg=BGS[(i * 3) % 8]))
    return todo


if __name__ == "__main__":
    todo = plan()
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for t in todo:
        open(os.path.join(OUT, f"{t['id']}.svg"), "w").write(svg(t["bg"], SCENES[t["scene"]](t["dish"], t["v"])))
        txt = re.sub(rf"^{re.escape(t['id'])} — .*\n", "", txt, flags=re.M) + f"{t['id']} — {DISH_RU[t['dish']]} {SCENE_RU[t['scene']]}\n"
    open(reg, "w").write(txt)
    json.dump([t["id"] for t in todo], open("/tmp/claude-0/cafe_ids.json", "w"))
    from collections import Counter
    print(len(todo), Counter(t["scene"] for t in todo).most_common(3), Counter(t["dish"] for t in todo).most_common(5))
