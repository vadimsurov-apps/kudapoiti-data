"""Иконки робота sections (2026-11-06, ночь), метод «Якорь + Характер + Шутка» в виде СЦЕН (урок бассейнов и падела:
не «один предмет + разные шапки», а герой-якорь × сцена из жизни секции). Герои: волейбольный/баскетбольный/футбольный/
теннисный мяч, волан, ракетка, шахматные конь/пешка/король, фехтовальная маска, ракетка для настольного тенниса,
шиповка, парусник, кимоно, шайба, гимнастка, пуанты, пачка. Сцены — только про спорт: пьедестал, кубок, медаль,
прыжок, малыш рядом, финишная ленточка, штанга, скамейка запасных, табло, секундомер, вымпел, лавровый венок, «дай пять»,
луч прожектора, конфетти, сетка, ворота, лёд, песок пляжа. Пара «герой + сцена» уникальна (сверено с icons-src/subjects.txt
и листами icons-catalog/sheet-01..26). Бассейны — сцены из tools/icons_pools_v2_1106.py с неиспользованными парами.
Запуск: python3 tools/icons_sections_1107.py"""
import os, re, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
import icons_pools_v2_1106 as PV
import add_sections_1107 as E

W = lambda w: s(f'stroke-width="{w}"')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
PINK, GOLD, RED, BLUE, YEL, GRN = "#FF7FA8", "#FFC93C", "#E8554A", "#5CB7F2", "#FFD25E", "#7CD26E"
F = lambda x, y, d=9, k=0.8, **kw: face(x, y, d=d, k=k, **kw)


def g(body, x, y, k=1.0, rot=0, flip=False):
    sx = -k if flip else k
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sx} {k})">{body}</g>'


# =====================  ГЕРОИ (вокруг 0,0, примерно ±34)  =====================
def vball():
    return (f'<circle r="34" fill="#fff" {W(3)}/><clipPath id="vbc"><circle r="34"/></clipPath><g clip-path="url(#vbc)">'
            f'<path d="M0 0 Q-22 -12 -26 -36 L-60 -30 V10 Q-30 -2 0 0Z" fill="{YEL}" {W(2.4)}/>'
            f'<path d="M0 0 Q24 -6 40 12 L42 50 H14 Q20 22 0 0Z" fill="{BLUE}" {W(2.4)}/>'
            f'<path d="M0 0 Q-4 24 -22 34" fill="none" {W(2.4)}/></g><circle r="34" fill="none" {W(3)}/>' + F(0, 2))


def bball():
    return (f'<circle r="34" fill="#F28C38" {W(3)}/><path d="M-34 0 H34 M0 -34 V34" fill="none" {W(2.4)}/>'
            f'<path d="M-22 -26 Q-8 0 -22 26 M22 -26 Q8 0 22 26" fill="none" {W(2.4)}/>' + F(0, 4))


def sball():
    pent = lambda x, y, r: ("M" + " L".join(f"{x + r * __import__('math').sin(a * 1.2566):.1f} {y - r * __import__('math').cos(a * 1.2566):.1f}" for a in range(5)) + "Z")
    return (f'<circle r="34" fill="#fff" {W(3)}/><clipPath id="sbc"><circle r="34"/></clipPath><g clip-path="url(#sbc)">'
            f'<path d="{pent(0, -16, 11)}" fill="{O}"/><path d="{pent(-34, 6, 11)}" fill="{O}"/><path d="{pent(34, 6, 11)}" fill="{O}"/>'
            f'<path d="{pent(-16, 36, 11)}" fill="{O}"/><path d="{pent(16, 36, 11)}" fill="{O}"/></g><circle r="34" fill="none" {W(3)}/>'
            + F(0, 10, d=9, k=0.75))


def tball():
    return (f'<circle r="32" fill="#D7F25A" {W(3)}/><path d="M-28 -16 Q-8 0 -28 16 M28 -16 Q8 0 28 16" fill="none" stroke="#fff" stroke-width="3.4"/>'
            + F(0, 2))


def racket():
    return (f'<path d="M0 22 V44" stroke="{O}" stroke-width="12" stroke-linecap="round"/><path d="M0 24 V44" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="-8" rx="24" ry="30" fill="#fff" {W(3)}/>'
            + "".join(f'<path d="M{x} -36 V20" stroke="#C9CDD8" stroke-width="1.6"/>' for x in range(-16, 20, 8))
            + "".join(f'<path d="M-22 {y} H22" stroke="#C9CDD8" stroke-width="1.6"/>' for y in range(-28, 16, 8))
            + f'<ellipse cx="0" cy="-8" rx="24" ry="30" fill="none" stroke="{O}" stroke-width="7"/>'
            f'<ellipse cx="0" cy="-8" rx="24" ry="30" fill="none" stroke="{BLUE}" stroke-width="3.4"/>' + F(0, -8, d=8, k=0.7))


def shuttle():
    return (f'<path d="M-12 8 L-30 -40 Q0 -50 30 -40 L12 8Z" fill="#fff" {W(3)}/>'
            + "".join(f'<path d="M{dx * 0.4:.0f} 8 L{dx} -42" stroke="#B8BCCB" stroke-width="2"/>' for dx in (-20, -10, 0, 10, 20))
            + f'<path d="M-24 -22 Q0 -28 24 -22" fill="none" stroke="#B8BCCB" stroke-width="2.4"/>'
            f'<path d="M-16 6 H16 V14 H-16Z" fill="{RED}" {W(2.4)}/><path d="M-16 14 Q-16 40 0 40 Q16 40 16 14Z" fill="#FFE9C9" {W(3)}/>'
            + F(0, 24, d=7, k=0.62))


def knight(dark=False):
    c, c2 = ("#4A4466", "#6A6488") if dark else ("#FFF7EC", "#E9DCC8")
    b = (f'<rect x="-30" y="34" width="60" height="12" rx="4" fill="{c}" {W(3)}/>'
         f'<rect x="-22" y="22" width="44" height="14" rx="3" fill="{c2}" {W(3)}/>'
         f'<path d="M-18 22 C-24 2 -20 -18 -10 -30 L-14 -46 L0 -36 C20 -38 34 -24 32 -6 L20 -4 C12 -4 8 0 12 8 C16 14 20 18 22 22Z" fill="{c}" {W(3)}/>'
         f'<path d="M-6 -32 Q-14 -16 -12 2" fill="none" stroke="{c2}" stroke-width="5"/>')
    ew = "#fff" if dark else O
    return b + (f'<ellipse cx="10" cy="-22" rx="4.4" ry="5.2" fill="{ew}"/><circle cx="8.6" cy="-24" r="1.7" fill="{c if dark else "#fff"}"/>'
                f'<ellipse cx="18" cy="-12" rx="5" ry="3" fill="{PINK}" opacity=".7"/><circle cx="28" cy="-10" r="1.6" fill="{O}"/>')


def pawn():
    c = "#FFF7EC"
    return (f'<rect x="-30" y="34" width="60" height="12" rx="4" fill="{c}" {W(3)}/>'
            f'<path d="M-24 36 Q-18 12 -10 2 H10 Q18 12 24 36Z" fill="{c}" {W(3)}/>'
            f'<rect x="-17" y="-4" width="34" height="9" rx="4" fill="#E9DCC8" {W(3)}/><circle cx="0" cy="-24" r="21" fill="{c}" {W(3)}/>'
            + F(0, -24, d=8, k=0.65))


def king():
    c = "#4A4466"
    return (f'<rect x="-30" y="34" width="60" height="12" rx="4" fill="{c}" {W(3)}/>'
            f'<path d="M-22 36 Q-16 6 -18 -14 H18 Q16 6 22 36Z" fill="{c}" {W(3)}/>'
            f'<rect x="-22" y="-20" width="44" height="9" rx="4" fill="#6A6488" {W(3)}/>'
            f'<path d="M-16 -20 Q0 -40 16 -20Z" fill="{c}" {W(3)}/><path d="M0 -50 V-30 M-8 -42 H8" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M0 -50 V-30 M-8 -42 H8" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>'
            f'<ellipse cx="-7" cy="6" rx="3.6" ry="4.4" fill="#fff"/><ellipse cx="7" cy="6" rx="3.6" ry="4.4" fill="#fff"/>'
            f'<circle cx="-7" cy="7" r="1.8" fill="{O}"/><circle cx="7" cy="7" r="1.8" fill="{O}"/>'
            f'<path d="M-4 14 Q0 18 4 14" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>'
            f'<ellipse cx="-13" cy="13" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/><ellipse cx="13" cy="13" rx="3.4" ry="2" fill="{PINK}" opacity=".8"/>')


def fmask():
    return (f'<path d="M-22 26 Q-22 44 0 46 Q22 44 22 26Z" fill="#fff" {W(3)}/>'
            f'<ellipse rx="28" ry="32" fill="#4A4466" {W(3)}/><clipPath id="fmc"><ellipse rx="25" ry="29"/></clipPath><g clip-path="url(#fmc)">'
            + "".join(f'<path d="M{x} -40 V40" stroke="#8A85A6" stroke-width="1.6"/>' for x in range(-26, 30, 6))
            + "".join(f'<path d="M-30 {y} H30" stroke="#8A85A6" stroke-width="1.6"/>' for y in range(-30, 34, 6)) + '</g>'
            f'<ellipse rx="28" ry="32" fill="none" stroke="#fff" stroke-width="3"/><ellipse rx="28" ry="32" fill="none" {W(2)}/>'
            f'<ellipse cx="-9" cy="-2" rx="5" ry="6" fill="#fff"/><ellipse cx="9" cy="-2" rx="5" ry="6" fill="#fff"/>'
            f'<circle cx="-9" cy="-1" r="2.4" fill="{O}"/><circle cx="9" cy="-1" r="2.4" fill="{O}"/>'
            f'<path d="M-5 11 Q0 16 5 11" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>')


def ttpaddle():
    return (f'<path d="M14 18 L30 40" stroke="{O}" stroke-width="15" stroke-linecap="round"/><path d="M14 18 L30 40" stroke="#C08A5A" stroke-width="9" stroke-linecap="round"/>'
            f'<circle cx="-4" cy="-6" r="30" fill="{RED}" {W(3)}/>' + F(-4, -6))


def sneaker():
    return (f'<path d="M-36 4 Q-36 -14 -24 -16 L-14 -34 H6 L10 -12 Q30 -8 38 6 V16 H-36Z" fill="#FF8FB8" {W(3)}/>'
            f'<path d="M-36 16 H38 V22 Q38 26 34 26 H-32 Q-36 26 -36 22Z" fill="#fff" {W(3)}/>'
            + "".join(f'<path d="M{x} 26 l2 7" {W(2.4)}/>' for x in (-26, -14, -2, 10, 22))
            + f'<path d="M-10 -26 l12 4 M-12 -18 l12 4" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
            f'<path d="M14 -6 Q24 2 30 2" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>' + F(-18, 2, d=7, k=0.62))


def sail():
    return (f'<path d="M2 -46 V18" {W(3.4)}/><path d="M4 -42 L36 12 H4Z" fill="#fff" {W(3)}/><path d="M0 -36 L-28 10 H0Z" fill="{YEL}" {W(3)}/>'
            f'<path d="M-38 18 H40 Q34 38 16 38 H-18 Q-34 38 -38 18Z" fill="{RED}" {W(3)}/>' + F(0, 27, d=11, k=0.62))


def kimono(c="#fff", belt=O):
    return (f'<path d="M-18 -34 L-44 -20 L-36 4 L-24 -2 L-24 38 H24 L24 -2 L36 4 L44 -20 L18 -34 Q0 -26 -18 -34Z" fill="{c}" {W(3)}/>'
            f'<path d="M-18 -34 L4 8 M18 -34 L-2 0" fill="none" {W(2.6)}/>'
            f'<rect x="-26" y="10" width="52" height="9" rx="2" fill="{belt}" {W(2.2)}/>'
            f'<path d="M-4 18 L-12 34 L-4 34 L0 22 L4 34 L12 34 L4 18Z" fill="{belt}" {W(2)}/>'
            + F(0, -10, d=8, k=0.62))


def puck():
    return (f'<path d="M30 -46 L10 20 Q8 28 -4 28 L-30 28" fill="none" stroke="{O}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M30 -46 L10 20 Q8 28 -4 28 L-30 28" fill="none" stroke="#E8B06E" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M-36 -2 V12 Q-36 22 -8 22 Q20 22 20 12 V-2Z" fill="#2E3446" {W(3)}/><ellipse cx="-8" cy="-2" rx="28" ry="10" fill="#4A5068" {W(3)}/>'
            + face(-8, 8, d=8, k=0.6).replace(f'fill="{O}"', 'fill="#fff"', 2))


def gymkid():
    return (f'<path d="M-6 0 L-30 -38 M6 0 L30 -38" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-6 0 L-30 -38 M6 0 L30 -38" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M-6 26 L-26 44 M6 26 L26 44" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-6 26 L-26 44 M6 26 L26 44" stroke="#FFD9B8" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M-12 -2 H12 L10 28 H-10Z" fill="#A98BF0" {W(3)}/><path d="M-10 20 L0 28 L10 20" fill="none" stroke="#fff" stroke-width="2"/>'
            f'<circle cx="0" cy="-16" r="14" fill="#FFD9B8" {W(3)}/><path d="M-14 -18 Q-12 -32 0 -32 Q12 -32 14 -18 Q8 -26 -14 -18Z" fill="#8A5A3C" {W(2.4)}/>'
            f'<circle cx="10" cy="-32" r="5" fill="#8A5A3C" {W(2.2)}/>' + F(0, -14, d=5, k=0.42))


def beam():
    return (f'<path d="M-24 6 L-30 40 M24 6 L30 40" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M-24 6 L-30 40 M24 6 L30 40" stroke="#B8BCCB" stroke-width="4" stroke-linecap="round"/>'
            f'<rect x="-44" y="-10" width="88" height="18" rx="6" fill="#E8B06E" {W(3)}/>' + F(0, -2, d=10, k=0.55))


def ballerina():
    skin = "#FFD9B8"
    return (f'<path d="M-8 -20 Q-30 -40 -12 -52 M8 -20 Q30 -40 12 -52" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-8 -20 Q-30 -40 -12 -52 M8 -20 Q30 -40 12 -52" fill="none" stroke="{skin}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M-4 18 L-6 46 M4 18 L18 40" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M-4 18 L-6 46 M4 18 L18 40" stroke="#FFC6DA" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M-36 14 Q-30 2 -18 6 Q-10 -2 0 4 Q10 -2 18 6 Q30 2 36 14 Q30 26 18 22 Q10 30 0 24 Q-10 30 -18 22 Q-30 26 -36 14Z" fill="#FFD1E3" {W(3)}/>'
            f'<path d="M-11 -18 H11 L9 8 H-9Z" fill="#FF8FB8" {W(3)}/>'
            f'<circle cx="0" cy="-30" r="12" fill="{skin}" {W(3)}/><path d="M-12 -32 Q-10 -44 0 -44 Q10 -44 12 -32 Q6 -40 -12 -32Z" fill="#8A5A3C" {W(2.2)}/>'
            f'<circle cx="0" cy="-46" r="5" fill="#8A5A3C" {W(2.2)}/>' + F(0, -29, d=5, k=0.4))


def tutu():
    import math
    pts = []
    for i in range(25):
        a = math.pi * 2 * i / 24
        r = 1.0 if i % 2 == 0 else 0.82
        pts.append(f"{46 * r * math.cos(a):.1f} {12 + 12 * r * math.sin(a):.1f}")
    return (f'<path d="M-6 18 L-8 46 M6 18 L8 46" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
            f'<path d="M-6 18 L-8 46 M6 18 L8 46" stroke="#FFC6DA" stroke-width="4.4" stroke-linecap="round"/>'
            f'<path d="M{pts[0]} L' + " L".join(pts[1:]) + f'Z" fill="#FFD1E3" {W(2.8)}/>'
            f'<ellipse cx="0" cy="10" rx="30" ry="6" fill="#FFE6EF"/>'
            f'<path d="M-16 -36 Q-6 -28 0 -34 Q6 -28 16 -36 L13 10 H-13Z" fill="#FF8FB8" {W(3)}/>'
            f'<path d="M-14 -34 L-11 -50 M14 -34 L11 -50" {W(2.6)}/>'
            + F(0, -14, d=6, k=0.52) + sparkle(34, -30, 6))


HERO = dict(vball=vball, bball=bball, sball=sball, tball=tball, racket=racket, shuttle=shuttle, knight=knight,
            knightd=lambda: knight(True), pawn=pawn, king=king, fmask=fmask, ttpaddle=ttpaddle, sneaker=sneaker, sail=sail,
            kimono=kimono, kimonob=lambda: kimono("#4C8EE8", "#fff"), kimonor=lambda: kimono("#E8554A", "#fff"), puck=puck,
            gymkid=gymkid, beam=beam, ballerina=ballerina, tutu=tutu)
HERO_RU = dict(vball="волейбольный мяч-персонаж", bball="баскетбольный мяч-персонаж", sball="футбольный мяч-персонаж",
               tball="теннисный мяч-персонаж", racket="теннисная ракетка-персонаж", shuttle="волан-персонаж",
               knight="белый шахматный конь-персонаж", knightd="тёмный шахматный конь-персонаж", pawn="белая пешка-персонаж",
               king="шахматный король-персонаж", fmask="фехтовальная маска-персонаж", ttpaddle="ракетка для настольного тенниса-персонаж",
               sneaker="шиповка-персонаж", sail="парусник-персонаж", kimono="белое кимоно-персонаж", kimonob="синее кимоно-персонаж",
               kimonor="красная куртка самбо-персонаж", puck="шайба-персонаж с клюшкой", gymkid="гимнастка в прыжке «звёздочкой»",
               beam="гимнастическое бревно-персонаж", ballerina="маленькая балерина в пачке", tutu="балетная пачка-персонаж")


# =====================  СЦЕНЫ  =====================
def floor(c="#E8C9A0", y=104):
    return f'<path d="M0 {y} Q64 {y-8} 128 {y} V128 H0Z" fill="{c}" {W(2.6)}/>'


def S_podium(h, v):
    return (floor() + f'<rect x="38" y="84" width="52" height="30" rx="3" fill="{GOLD}" {W(3)}/>'
            f'<text x="64" y="108" font-family="Arial" font-weight="bold" font-size="20" text-anchor="middle" fill="{O}">1</text>'
            + g(HERO[h](), 64, 50, 0.82) + sparkle(22, 40, 6) + sparkle(106, 34, 5))


def cup(x, y, k=1.0):
    return g(f'<path d="M-16 -22 H16 Q16 4 0 8 Q-16 4 -16 -22Z" fill="{GOLD}" {W(3)}/>'
             f'<path d="M-16 -16 Q-28 -16 -26 -6 Q-24 2 -12 2 M16 -16 Q28 -16 26 -6 Q24 2 12 2" fill="none" {W(3)}/>'
             f'<rect x="-4" y="8" width="8" height="10" fill="{GOLD}" {W(2.4)}/><rect x="-12" y="18" width="24" height="7" rx="2" fill="#C08A5A" {W(2.4)}/>', x, y, k)


def S_trophy(h, v):
    left = v % 2
    return floor() + g(HERO[h](), 48 if not left else 80, 66, 0.78) + cup(98 if not left else 30, 70, 1.15) + sparkle(98 if not left else 30, 30, 6)


def S_medal(h, v):
    return (g(HERO[h](), 64, 58, 0.86) + f'<path d="M48 70 L64 96 L80 70" fill="none" stroke="{RED}" stroke-width="5"/>'
            f'<circle cx="64" cy="100" r="13" fill="{GOLD}" {W(2.8)}/>'
            f'<text x="64" y="106" font-family="Arial" font-weight="bold" font-size="15" text-anchor="middle" fill="{O}">1</text>')


def S_jump(h, v):
    return (floor("#C9E8B8" if v % 2 else "#E8C9A0") + f'<ellipse cx="64" cy="110" rx="22" ry="5" fill="{O}" opacity=".18"/>'
            f'<path d="M30 90 Q26 76 32 66 M98 90 Q102 76 96 66" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
            + g(HERO[h](), 64, 50, 0.8, -10 if v % 2 else 10) + sparkle(24, 30, 6) + sparkle(104, 26, 5))


def S_duo(h, v):
    return floor() + g(HERO[h](), 50, 60, 0.82) + g(HERO[h](), 100, 88, 0.42, flip=True) + sparkle(104, 40, 6)


def S_spot(h, v):
    return (f'<path d="M52 0 L20 112 H108 L76 0Z" fill="#FFF6C4" opacity=".75"/><ellipse cx="64" cy="108" rx="40" ry="8" fill="#FFF6C4" {W(2.4)}/>'
            + g(HERO[h](), 64, 66, 0.82) + sparkle(22, 30, 5) + sparkle(106, 40, 6))


def S_confetti(h, v):
    rnd = random.Random(v + 3)
    bits = "".join(f'<rect x="{rnd.randint(14, 110)}" y="{rnd.randint(14, 50)}" width="6" height="10" rx="2" fill="{c}" '
                   f'transform="rotate({rnd.randint(-40, 40)} 64 64)"/>' for c in [RED, BLUE, YEL, GRN, PINK, "#A98BF0"] * 2)
    return bits + g(HERO[h](), 64, 72, 0.86)


def S_barbell(h, v):
    return (floor() + g(HERO[h](), 64, 74, 0.72)
            + f'<path d="M48 54 L40 32 M80 54 L88 32" stroke="{O}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M14 30 H114" stroke="{O}" stroke-width="7" stroke-linecap="round"/><path d="M14 30 H114" stroke="#B8BCCB" stroke-width="3"/>'
            f'<rect x="16" y="16" width="12" height="28" rx="3" fill="{RED}" {W(2.6)}/><rect x="100" y="16" width="12" height="28" rx="3" fill="{RED}" {W(2.6)}/>')


def S_finish(h, v):
    return (floor("#E86A5A", 106) + f'<path d="M14 40 V112 M114 40 V112" {W(4)}/>'
            f'<path d="M14 66 Q40 74 56 62 M72 62 Q90 74 114 66" fill="none" stroke="{O}" stroke-width="6"/>'
            f'<path d="M14 66 Q40 74 56 62 M72 62 Q90 74 114 66" fill="none" stroke="#fff" stroke-width="3"/>'
            + g(HERO[h](), 64, 64, 0.72) + sparkle(30, 28, 5) + sparkle(98, 26, 5))


def S_bench(h, v):
    return (floor() + f'<rect x="16" y="86" width="96" height="10" rx="3" fill="#E8B06E" {W(2.6)}/>'
            f'<path d="M26 96 V112 M102 96 V112" {W(4)}/>' + g(HERO[h](), 64, 56, 0.8)
            + f'<path d="M94 58 q8 -4 16 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')


def S_score(h, v):
    a, b = [(3, 2), (2, 1), (5, 4), (1, 0)][v % 4]
    return (f'<rect x="28" y="12" width="72" height="30" rx="6" fill="#2E3446" {W(3)}/>'
            f'<text x="64" y="35" font-family="Arial" font-weight="bold" font-size="20" text-anchor="middle" fill="{YEL}">{a}:{b}</text>'
            + g(HERO[h](), 64, 82, 0.72))


def S_watch(h, v):
    return (floor() + g(HERO[h](), 54, 70, 0.8)
            + f'<circle cx="98" cy="36" r="20" fill="#fff" {W(3)}/><rect x="93" y="10" width="10" height="7" rx="2" fill="{RED}" {W(2.4)}/>'
            + "".join(f'<path d="M98 20 V23" {W(2)} transform="rotate({a} 98 36)"/>' for a in range(0, 360, 45))
            + f'<path d="M98 36 L108 26" {W(3)}/>')


def S_pennant(h, v):
    c = [BLUE, RED, GRN, "#A98BF0"][v % 4]
    return (g(HERO[h](), 56, 68, 0.82) + f'<path d="M92 112 V24" {W(4)}/><path d="M92 24 L122 38 L92 52Z" fill="{c}" {W(2.6)}/>'
            + sparkle(24, 28, 6))


def S_wreath(h, v):
    leaves = "".join(f'<ellipse cx="{64 + 46 * __import__("math").cos(a):.1f}" cy="{64 + 46 * __import__("math").sin(a):.1f}" rx="8" ry="4" '
                     f'fill="{GRN}" {W(1.8)} transform="rotate({a * 57.3 + 60:.0f} {64 + 46 * __import__("math").cos(a):.1f} {64 + 46 * __import__("math").sin(a):.1f})"/>'
                     for a in [i * 0.33 + 0.3 for i in range(8)] + [3.14 - i * 0.33 - 0.3 for i in range(8)])
    return leaves + f'<path d="M58 112 L64 104 L70 112" fill="{RED}" {W(2)}/>' + g(HERO[h](), 64, 62, 0.8)


def S_five(h, v):
    return (floor() + g(HERO[h](), 40, 70, 0.62, 10) + g(HERO[h](), 90, 70, 0.62, -10, flip=True)
            + sparkle(64, 30, 9) + sparkle(46, 22, 4) + sparkle(84, 22, 4))


def S_hug(h, v):
    mate = {"vball": "sball", "bball": "vball", "sball": "bball", "tball": "racket", "racket": "tball", "shuttle": "racket"}.get(h, h)
    return (floor() + g(HERO[h](), 46, 70, 0.66, 8) + g(HERO[mate](), 84, 70, 0.62, -8)
            + f'<path d="M64 26 C58 16 46 22 52 32 L64 42 L76 32 C82 22 70 16 64 26Z" fill="{PINK}" {W(2.4)}/>')


def S_net(h, v):
    return (f'<rect x="4" y="80" width="120" height="30" fill="none" {W(2)}/>'
            + "".join(f'<path d="M{x} 80 V110" stroke="#fff" stroke-width="2"/>' for x in range(14, 120, 10))
            + "".join(f'<path d="M4 {y} H124" stroke="#fff" stroke-width="2"/>' for y in (90, 100))
            + f'<rect x="2" y="76" width="124" height="6" fill="#fff" {W(2.2)}/>' + g(HERO[h](), 64, 44, 0.72))


def S_goal(h, v):
    return (floor("#8FDB7A") + f'<path d="M14 100 V36 H114 V100" fill="none" stroke="{O}" stroke-width="8" stroke-linejoin="round"/>'
            f'<path d="M14 100 V36 H114 V100" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"/>'
            + "".join(f'<path d="M{x} 40 V98" stroke="#fff" stroke-width="1.4" opacity=".8"/>' for x in range(24, 112, 10))
            + "".join(f'<path d="M18 {y} H110" stroke="#fff" stroke-width="1.4" opacity=".8"/>' for y in range(46, 100, 10))
            + g(HERO[h](), 64, 74, 0.7))


def S_ice(h, v):
    return (f'<path d="M0 96 Q64 86 128 96 V128 H0Z" fill="#E9F7FF" {W(2.6)}/>'
            f'<path d="M20 108 q20 -6 40 0 M70 114 q20 -6 40 0" fill="none" stroke="#9DD6F5" stroke-width="3" stroke-linecap="round"/>'
            + g(HERO[h](), 64, 58, 0.82) + sparkle(24, 30, 5))


def S_beach(h, v):
    return (f'<circle cx="104" cy="26" r="12" fill="{YEL}" {W(2.6)}/><path d="M0 98 Q64 86 128 98 V128 H0Z" fill="#F7D98B" {W(2.6)}/>'
            f'<path d="M14 96 V60 M114 96 V60" {W(3)}/><path d="M14 64 H114" stroke="{O}" stroke-width="2"/>'
            + g(HERO[h](), 60, 64, 0.72))


def S_crown(h, v):
    return (g(HERO[h](), 64, 72, 0.86)
            + f'<path d="M44 34 L48 14 L58 26 L64 10 L70 26 L80 14 L84 34Z" fill="{GOLD}" {W(2.6)}/>' + sparkle(22, 30, 5))


def S_grad(h, v):
    return (g(HERO[h](), 64, 72, 0.86) + f'<path d="M36 26 L64 14 L92 26 L64 38Z" fill="#2E3446" {W(2.6)}/>'
            f'<path d="M50 32 V42 Q64 48 78 42 V32" fill="#2E3446" {W(2.6)}/><path d="M92 26 V40" stroke="{GOLD}" stroke-width="3"/>'
            f'<circle cx="92" cy="42" r="3" fill="{GOLD}"/>')


SCENES = dict(podium=S_podium, trophy=S_trophy, medal=S_medal, jump=S_jump, duo=S_duo, spot=S_spot, confetti=S_confetti,
              barbell=S_barbell, finish=S_finish, bench=S_bench, score=S_score, watch=S_watch, pennant=S_pennant,
              wreath=S_wreath, five=S_five, hug=S_hug, net=S_net, goal=S_goal, ice=S_ice, beach=S_beach, crown=S_crown, grad=S_grad)
SCENE_RU = dict(podium="на пьедестале «1»", trophy="рядом с золотым кубком", medal="с золотой медалью «1» на ленте",
                jump="в высоком прыжке", duo="с малышом-копией рядом", spot="в луче прожектора на сцене",
                confetti="под конфетти после победы", barbell="поднимает штангу на разминке", finish="рвёт финишную ленточку",
                bench="ждёт выхода на скамейке запасных", score="под табло со счётом", watch="на фоне секундомера",
                pennant="с вымпелом команды", wreath="в лавровом венке", five="«дай пять» с другом-близнецом",
                hug="обнимается с напарником", net="над сеткой", goal="в футбольных воротах", ice="на льду катка",
                beach="на пляжной площадке с сеткой", crown="в короне чемпиона", grad="в шапке выпускника")

ANCH = {"badminton": ["shuttle"], "ballgames": ["vball", "bball"], "chess": ["knight", "knightd", "pawn", "king"],
        "martial": ["kimono", "kimonob", "kimonor"], "gymnastics": ["gymkid"], "racket": ["racket", "tball"],
        "hockey": ["puck"], "football": ["sball"], "dance": ["ballerina", "tutu"]}
# сцены, которые не подходят герою
BAN = {"net": lambda h: h not in ("vball", "shuttle", "tball"), "goal": lambda h: h != "sball",
       "ice": lambda h: h not in ("puck",), "crown": lambda h: h in ("gymkid", "ballerina"), "grad": lambda h: h in ("gymkid", "ballerina"), "jump": lambda h: h in ("gymkid", "ballerina"), "beach": lambda h: h != "vball", "barbell": lambda h: h in ("beam", "sail", "gymkid", "ballerina", "tutu"),
       "hug": lambda h: h not in ("vball", "bball", "sball", "tball", "racket", "shuttle"),
       "score": lambda h: h in ("ballerina", "tutu", "beam", "gymkid", "sail"), "goal_": None}


def anchors(r):
    pid, c = r["id"], r["Категории"]
    if c == "sport":
        for k, h in [("fenc", "fmask"), ("table-tennis", "ttpaddle"), ("athletics", "sneaker"), ("sailing", "sail")]:
            if k in pid: return [h]
        raise ValueError(pid)
    if c == "ballgames":
        if "basket" in pid: return ["bball"]
        return ["vball"]
    return ANCH[c]


PREF = {"beach-volleyball": "beach", "rusvolley": "net", "grossmeyster": "crown", "akadem": "grad", "rba-basket-skolka": "grad",
        "footlandiya": "duo", "triumf": "podium", "hockeyway": "ice", "fenomen": "spot", "sovenok": "grad"}


def plan():
    reg = open(os.path.join(OUT, "subjects.txt")).read()
    rnd = random.Random(1107)
    used, sc_n, hero_n, todo = set(), {}, {}, []
    BGS = ["sky", "teal", "yellow", "pink", "purple", "orange", "green", "blue"]
    rows = [r for r in E.ROWS if r["Категории"] != "pools"]
    for i, r in enumerate(rows):
        opts = anchors(r)
        pref = next((v for k, v in PREF.items() if k in r["id"]), None)
        cands = []
        for h in opts:
            for sc in SCENES:
                f = BAN.get(sc)
                if f and f(h): continue
                phrase = f"{HERO_RU[h]} {SCENE_RU[sc]}"
                if (h, sc) in used or phrase in reg: continue
                cost = sc_n.get(sc, 0) * 3 + hero_n.get(h, 0) * 2 + rnd.random() * 2 - (5 if sc == pref and sc_n.get(sc, 0) < 3 else 0)
                cands.append((cost, h, sc, phrase))
        cost, h, sc, phrase = min(cands)
        used.add((h, sc)); sc_n[sc] = sc_n.get(sc, 0) + 1; hero_n[h] = hero_n.get(h, 0) + 1
        todo.append((r["id"], svg(BGS[(i * 3) % 8], SCENES[sc](h, sc_n[sc])), phrase))
    # бассейны: свободные пары из генератора бассейнов v2
    prow = [r for r in E.ROWS if r["Категории"] == "pools"]
    pused = set()
    for i, r in enumerate(prow):
        pref = ("surf", "rain", "ball", "fountain") if "shtorm" in r["id"] else ("podium", "trophy", "block", "diving")
        cands = []
        for sc in PV.SCENES:
            for h in PV.FIT[sc]:
                phrase = f"{PV.HERO_RU[h]} {PV.SCENE_RU[sc]}"
                if (sc, h) in pused or phrase in reg or h == "moray": continue
                cost = sc_n.get("p" + sc, 0) * 3 + hero_n.get("p" + h, 0) * 2 + rnd.random() * 2 - (4 if sc in pref else 0)
                cands.append((cost, sc, h, phrase))
        cost, sc, h, phrase = min(cands)
        pused.add((sc, h)); sc_n["p" + sc] = sc_n.get("p" + sc, 0) + 1; hero_n["p" + h] = hero_n.get("p" + h, 0) + 1
        todo.append((r["id"], svg(["sky", "teal", "yellow", "pink", "purple", "orange", "green", "blue"][(i * 5) % 8],
                                  PV.SCENES[sc](h, sc_n["p" + sc] - 1)), phrase))
    return todo


if __name__ == "__main__":
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for pid, body, phrase in plan():
        open(os.path.join(OUT, f"{pid}.svg"), "w").write(body)
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M) + f"{pid} — {phrase}\n"
    open(reg, "w").write(txt)
    print("ok")
