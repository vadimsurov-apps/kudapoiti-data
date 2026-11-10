"""Бассейны v2 (06.11, Вадим: «однообразно, везде бассейн, куча одинаковых китов в одних позах — включи фантазию,
все аватары уникальные»). Каждая иконка — своя СЦЕНА: свой герой + своё место/действие (вышка, горка, подводный мир,
льдина, кувшинка, аквариум, пьедестал, надувной фламинго, водопад, сёрф…) + свой размер/поза/фон.
Пара «место + герой» не повторяется; каждое место — не больше 5 раз и всегда с другим героем и другой раскладкой;
каждый герой — не больше 5 раз и всегда в другом месте."""
import json, math, os, re, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
BL, BL2, FOAM = "#5CB7F2", "#3E9BE0", "#BFE6FF"
PINK = "#FF7FA8"


def F(x, y, d=7, k=0.6, blush=True):
    return face(x, y, d=d, k=k, blush=blush)


def cheeks(x, y, d):
    return (f'<ellipse cx="{x-d}" cy="{y}" rx="3.6" ry="2.4" fill="{PINK}" opacity=".65"/>'
            f'<ellipse cx="{x+d}" cy="{y}" rx="3.6" ry="2.4" fill="{PINK}" opacity=".65"/>')


# =====================  ГЕРОИ (рисуются вокруг 0,0, размер ~ ±30)  =====================
def whale(c="#4C8EE8"):
    return (f'<path d="M22 6 Q40 2 40 -14 Q46 -22 50 -16 Q44 -10 50 -4 Q42 4 34 8Z" fill="{c}" {W(2.6)}/>'
            f'<ellipse cx="0" cy="0" rx="32" ry="26" fill="{c}" {s()}/>'
            f'<path d="M-26 10 Q0 30 26 10 Q0 20 -26 10Z" fill="#CFE6FF"/>' + F(-6, -2, 8, 0.65))


def dolphin(c="#6FA8DC"):
    return (f'<path d="M-30 22 Q-34 -10 -4 -22 Q18 -30 34 -18 L44 -16 Q38 -8 30 -8 Q14 -10 4 4 Q-6 18 -10 30Z" fill="{c}" {s()}/>'
            f'<path d="M-4 -22 Q0 -38 12 -34 Q4 -28 6 -20Z" fill="{c}" {W(2.4)}/>'
            f'<path d="M-30 22 L-42 18 L-36 30 L-24 34Z" fill="{c}" {W(2.4)}/>'
            f'<path d="M4 -6 Q20 -16 30 -8 Q16 -4 8 6Z" fill="#DCEBFA"/>'
            + eye(18, -18, 0.7) + f'<path d="M30 -12 Q36 -9 42 -13" fill="none" stroke="{O}" stroke-width="2"/>'
            + f'<ellipse cx="14" cy="-11" rx="3.4" ry="2" fill="{PINK}" opacity=".6"/>')


def orca():
    return (dolphin("#2E3446").replace('fill="#DCEBFA"', 'fill="#fff"')
            + f'<ellipse cx="17" cy="-19" rx="6" ry="3.6" fill="#fff" transform="rotate(-15 17 -19)"/>' + eye(18, -18, 0.6))


def seal(c="#9AA7B8"):
    return (f'<path d="M-6 20 Q-36 26 -40 10 Q-30 14 -22 8" fill="{c}" {W(2.4)}/>'
            f'<ellipse cx="-4" cy="10" rx="30" ry="18" fill="{c}" {s()}/>'
            f'<circle cx="14" cy="-8" r="20" fill="{c}" {s()}/>'
            f'<path d="M-2 22 L-10 32 L4 28Z" fill="{c}" {W(2)}/>'
            + F(14, -12, 7, 0.55)
            + f'<ellipse cx="14" cy="-1" rx="7" ry="5" fill="#C9D3DF" {W(1.4)}/><ellipse cx="14" cy="-4" rx="2.8" ry="2" fill="{O}"/>'
            + "".join(f'<path d="M{14+sg*6} -1 L{14+sg*17} {dy}" stroke="{O}" stroke-width="1.3"/>' for sg in (-1, 1) for dy in (-4, 1)))


def walrus():
    return (seal("#C98A5E")
            + f'<path d="M9 0 L7 14 L12 1Z M19 0 L21 14 L16 1Z" fill="#FFF8E8" {W(1.6)}/>'
            + f'<ellipse cx="9" cy="-2" rx="7" ry="5.5" fill="#E0B088" {W(1.6)}/><ellipse cx="19" cy="-2" rx="7" ry="5.5" fill="#E0B088" {W(1.6)}/>'
            + f'<ellipse cx="14" cy="-5" rx="2.8" ry="2" fill="{O}"/>')


def otter():   # калан лежит на спинке
    return (f'<ellipse cx="0" cy="4" rx="34" ry="16" fill="#A8693E" {s()}/>'
            f'<ellipse cx="2" cy="6" rx="22" ry="10" fill="#C98A5E"/>'
            f'<circle cx="-24" cy="-6" r="5" fill="#A8693E" {W(2)}/><circle cx="-6" cy="-12" r="5" fill="#A8693E" {W(2)}/>'
            f'<circle cx="-16" cy="-4" r="15" fill="#A8693E" {s()}/><ellipse cx="-16" cy="0" rx="11" ry="9" fill="#F2D3AE"/>'
            + F(-16, -6, 6, 0.5) + f'<ellipse cx="-16" cy="-1" rx="3" ry="2.2" fill="{O}"/>'
            + f'<ellipse cx="8" cy="-8" rx="6" ry="4" fill="#A8693E" {W(1.8)}/><ellipse cx="18" cy="-6" rx="6" ry="4" fill="#A8693E" {W(1.8)}/>'
            + f'<ellipse cx="32" cy="0" rx="6" ry="4" fill="#A8693E" {W(1.8)}/>')


def penguin():
    return (f'<ellipse cx="0" cy="6" rx="22" ry="27" fill="#2E3446" {s()}/>'
            f'<ellipse cx="0" cy="10" rx="15" ry="21" fill="#fff"/>'
            f'<path d="M-15 -8 Q0 -16 15 -8 Q12 6 0 8 Q-12 6 -15 -8Z" fill="#fff"/>'
            f'<path d="M-20 0 Q-32 10 -26 20" fill="#2E3446" {W(2.4)}/><path d="M20 0 Q32 10 26 20" fill="#2E3446" {W(2.4)}/>'
            f'<path d="M-10 32 H-2 M2 32 H10" stroke="#FFB020" stroke-width="5" stroke-linecap="round"/>'
            + eye(-6, -6, 0.65) + eye(6, -6, 0.65) + f'<path d="M-5 0 H5 L0 6Z" fill="#FFB020" {W(1.8)}/>' + cheeks(0, 0, 12))


def turtle():
    return (f'<ellipse cx="-30" cy="4" rx="8" ry="5" fill="#A6D98F" {W(2)}/>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="10" fill="#A6D98F" {W(2)} transform="rotate({a} {x} {y})"/>' for x, y, a in [(-16, 16, 30), (16, 16, -30), (-14, -12, -30), (14, -12, 30)])
            + f'<ellipse cx="0" cy="2" rx="24" ry="20" fill="#6BAE5A" {s()}/>'
            f'<path d="M-12 -8 L12 -8 L18 6 L0 16 L-18 6Z" fill="none" stroke="#4E8A40" stroke-width="2.6"/>'
            f'<circle cx="30" cy="0" r="12" fill="#A6D98F" {s()}/>' + F(31, -1, 5, 0.45))


def octopus(c="#FF8FB1"):
    legs = "".join(f'<path d="M{x} 8 Q{x+dx} 26 {x+dx*2} 22" fill="none" stroke="{O}" stroke-width="10" stroke-linecap="round"/>'
                   f'<path d="M{x} 8 Q{x+dx} 26 {x+dx*2} 22" fill="none" stroke="{c}" stroke-width="5.5" stroke-linecap="round"/>'
                   for x, dx in [(-16, -8), (-6, -4), (6, 4), (16, 8)])
    return (legs + f'<path d="M-24 6 Q-26 -28 0 -28 Q26 -28 24 6 Q24 16 0 16 Q-24 16 -24 6Z" fill="{c}" {s()}/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2.8" fill="#FFC2D6"/>' for x, y in [(-12, -18), (10, -20), (16, -8)]) + F(0, -2, 8, 0.6))


def clownfish():
    return (f'<path d="M24 0 L40 -14 Q36 0 40 14Z" fill="#FF8A3D" {s()}/>'
            f'<ellipse cx="0" cy="0" rx="28" ry="20" fill="#FF8A3D" {s()}/>'
            + "".join(f'<path d="M{x} -19 Q{x+6} 0 {x} 19" fill="none" stroke="{O}" stroke-width="9"/><path d="M{x} -19 Q{x+6} 0 {x} 19" fill="none" stroke="#fff" stroke-width="5"/>' for x in (-10, 10))
            + eye(-18, -4, 0.75) + f'<path d="M-27 6 Q-22 10 -17 6" fill="none" stroke="{O}" stroke-width="2"/>')


def crab():
    return ("".join(f'<path d="M{sg*14} 10 L{sg*26} 22" {W(4)}/><path d="M{sg*18} 4 L{sg*30} 12" {W(4)}/>' for sg in (-1, 1))
            + "".join(f'<path d="M{sg*18} -6 L{sg*28} -22" {W(4)}/><path d="M{sg*28} -22 q{sg*-8} -10 {sg*2} -14 q{sg*10} 2 {sg*6} 12 l{sg*-6} -4Z" fill="#E8554A" {W(2.4)}/>' for sg in (-1, 1))
            + f'<ellipse cx="0" cy="4" rx="22" ry="15" fill="#E8554A" {s()}/>'
            f'<path d="M-6 -8 V-16 M6 -8 V-16" {W(2.4)}/><circle cx="-6" cy="-18" r="4.5" fill="#fff" {W(2)}/><circle cx="6" cy="-18" r="4.5" fill="#fff" {W(2)}/>'
            f'<circle cx="-6" cy="-18" r="2" fill="{O}"/><circle cx="6" cy="-18" r="2" fill="{O}"/>'
            f'<path d="M-6 6 Q0 11 6 6" fill="none" {W(2)}/>' + cheeks(0, 4, 12))


def seahorse():
    return (f'<path d="M4 -26 Q20 -28 18 -14 Q16 -4 6 0 Q18 8 14 20 Q10 32 -2 30 Q-10 28 -6 22 Q2 24 4 18 Q6 10 -6 6 Q-12 -2 -8 -14 Q-6 -24 4 -26Z" fill="#FFC93C" {s()}/>'
            f'<path d="M16 -20 L28 -18 L28 -12 L16 -12Z" fill="#FFC93C" {W(2.4)}/>'
            f'<path d="M-8 -14 L-16 -10 L-8 -6 M-8 -4 L-16 0 L-8 2" fill="#FFE07A" {W(1.8)}/>' + eye(8, -18, 0.6)
            + f'<ellipse cx="10" cy="-10" rx="3" ry="2" fill="{PINK}" opacity=".7"/>')


def jelly():
    return ("".join(f'<path d="M{x} 6 Q{x+5} 18 {x} 30 Q{x-4} 38 {x+2} 44" fill="none" stroke="#B48CF0" stroke-width="3" stroke-linecap="round"/>' for x in (-14, -5, 4, 13))
            + f'<path d="M-24 8 Q-24 -24 0 -24 Q24 -24 24 8 Q12 4 0 8 Q-12 4 -24 8Z" fill="#D7C2FF" fill-opacity=".95" {s()}/>' + F(0, -6, 7, 0.55))


def starfish():
    pts = " ".join(f"{(26 if i % 2 == 0 else 11)*math.cos(-math.pi/2+i*math.pi/5):.1f},{(26 if i % 2 == 0 else 11)*math.sin(-math.pi/2+i*math.pi/5):.1f}" for i in range(10))
    return f'<polygon points="{pts}" fill="#FF9A5C" stroke="{O}" stroke-width="3" stroke-linejoin="round"/>' + "".join(
        f'<circle cx="{x}" cy="{y}" r="1.8" fill="#FFD2A8"/>' for x, y in [(0, -16), (-14, -4), (14, -4), (-8, 12), (8, 12)]) + F(0, 1, 6, 0.5)


def puffer():
    sp = "".join(f'<path d="M{24*math.cos(a):.1f} {24*math.sin(a):.1f} L{28*math.cos(a):.1f} {28*math.sin(a):.1f}" {W(2.4)}/>' for a in [i * math.pi / 6 + 0.26 for i in range(12)] if math.cos(a) < 0.7)
    return (sp + f'<path d="M20 0 L40 -14 Q34 0 40 14Z" fill="#FFB020" {s()}/><path d="M2 18 L10 30 L14 18Z" fill="#FFB020" {W(2)}/><circle r="24" fill="#FFD25E" {s()}/>'
            f'<ellipse cx="0" cy="10" rx="16" ry="9" fill="#FFF3C4"/>' + F(-4, -2, 8, 0.6)
            + f'<circle cx="-4" cy="9" r="3.2" fill="{O}"/>')


def frog():
    return (f'<ellipse cx="0" cy="12" rx="24" ry="16" fill="#7CD26E" {s()}/>'
            f'<ellipse cx="-12" cy="-12" rx="9" ry="9" fill="#7CD26E" {s()}/><ellipse cx="12" cy="-12" rx="9" ry="9" fill="#7CD26E" {s()}/>'
            f'<circle cx="-12" cy="-12" r="5" fill="#fff" {W(1.6)}/><circle cx="12" cy="-12" r="5" fill="#fff" {W(1.6)}/>'
            f'<circle cx="-11" cy="-11" r="2.6" fill="{O}"/><circle cx="13" cy="-11" r="2.6" fill="{O}"/>'
            f'<path d="M-12 6 Q0 16 12 6" fill="none" {W(2.4)}/>' + cheeks(0, 6, 17)
            + f'<path d="M-22 24 q-8 4 -12 0 M22 24 q8 4 12 0" fill="none" stroke="#5CB04F" stroke-width="5" stroke-linecap="round"/>')


def hippo():
    return (f'<ellipse cx="-14" cy="-22" rx="6" ry="5" fill="#B9A7D8" {W(2.2)}/><ellipse cx="14" cy="-22" rx="6" ry="5" fill="#B9A7D8" {W(2.2)}/>'
            f'<ellipse cx="0" cy="-4" rx="24" ry="20" fill="#B9A7D8" {s()}/>'
            f'<ellipse cx="0" cy="10" rx="20" ry="13" fill="#D3C6EA" {s()}/>'
            + eye(-9, -10, 0.65) + eye(9, -10, 0.65) + f'<ellipse cx="-7" cy="6" rx="2.4" ry="3" fill="{O}"/><ellipse cx="7" cy="6" rx="2.4" ry="3" fill="{O}"/>'
            + cheeks(0, 0, 18))


def polarbear():
    return (f'<circle cx="-14" cy="-20" r="6" fill="#F4F7FB" {W(2.4)}/><circle cx="14" cy="-20" r="6" fill="#F4F7FB" {W(2.4)}/>'
            f'<circle cx="0" cy="-4" r="20" fill="#F4F7FB" {s()}/><ellipse cx="0" cy="3" rx="9" ry="7" fill="#E3E9F2" {W(1.6)}/>'
            + F(0, -8, 7, 0.55) + f'<ellipse cx="0" cy="0" rx="3" ry="2.2" fill="{O}"/>'
            + f'<ellipse cx="-16" cy="14" rx="7" ry="5" fill="#F4F7FB" {W(2)}/><ellipse cx="16" cy="14" rx="7" ry="5" fill="#F4F7FB" {W(2)}/>')


def axolotl():
    gills = "".join(f'<path d="M{sg*16} {y} q{sg*10} {-4+dy} {sg*14} {dy}" fill="none" stroke="#FF5A8A" stroke-width="4" stroke-linecap="round"/>' for sg in (-1, 1) for y, dy in [(-10, -6), (-4, 0), (2, 6)])
    return (f'<path d="M10 10 Q34 14 38 28 Q24 24 8 20Z" fill="#FFB3CF" {W(2.4)}/>' + gills
            + f'<ellipse cx="0" cy="0" rx="20" ry="16" fill="#FFB3CF" {s()}/>' + F(0, -2, 7, 0.65)
            + f'<ellipse cx="-12" cy="16" rx="5" ry="4" fill="#FFB3CF" {W(1.8)}/><ellipse cx="12" cy="16" rx="5" ry="4" fill="#FFB3CF" {W(1.8)}/>')


def platypus():
    return (f'<path d="M14 6 Q36 8 38 -2 Q30 -6 18 -4Z" fill="#8A5530" {W(2.4)}/>'
            f'<ellipse cx="0" cy="2" rx="22" ry="17" fill="#A8693E" {s()}/>'
            f'<ellipse cx="-24" cy="4" rx="13" ry="7" fill="#3B3355" {s()}/>' + eye(-8, -6, 0.65) + eye(4, -6, 0.65)
            + f'<ellipse cx="-4" cy="2" rx="3.4" ry="2.2" fill="{PINK}" opacity=".7"/>')


def goldfish():
    return (f'<path d="M18 0 Q34 -20 40 -8 Q32 0 40 8 Q34 20 18 0Z" fill="#FFA53D" {s()}/>'
            f'<ellipse cx="0" cy="0" rx="22" ry="17" fill="#FFA53D" {s()}/>'
            f'<path d="M-4 -16 Q6 -28 12 -14Z" fill="#FFC27A" {W(2)}/>' + eye(-10, -4, 0.75) + f'<circle cx="-20" cy="4" r="2.6" fill="{O}"/>'
            + f'<ellipse cx="-6" cy="4" rx="3.6" ry="2.2" fill="{PINK}" opacity=".7"/>')


def shark():
    return (f'<path d="M-36 4 Q-10 -26 26 -10 Q38 -4 40 4 Q20 14 -10 12 Q-26 12 -36 4Z" fill="#8CA2B8" {s()}/>'
            f'<path d="M-6 -16 L4 -34 L10 -12Z" fill="#8CA2B8" {W(2.6)}/><path d="M-36 4 L-46 -10 L-44 12Z" fill="#8CA2B8" {W(2.4)}/>'
            f'<path d="M-20 8 Q10 16 38 4 Q10 6 -20 8Z" fill="#E8EEF5"/>'
            + eye(20, -6, 0.65) + f'<path d="M24 4 Q30 8 36 4" fill="none" {W(2)}/><path d="M26 5 L27 8 L29 5 L31 8 L33 5" fill="#fff" stroke="{O}" stroke-width="1"/>')


def beluga():
    return (f'<path d="M22 8 Q40 6 42 -8 Q48 -14 50 -6 Q46 0 50 8 Q40 12 30 12Z" fill="#E8F1FA" {W(2.6)}/>'
            f'<ellipse cx="0" cy="4" rx="30" ry="20" fill="#E8F1FA" {s()}/><ellipse cx="-14" cy="-10" rx="16" ry="12" fill="#E8F1FA" {s()}/>'
            + F(-14, -8, 7, 0.55))


def capybara():
    return (f'<rect x="-28" y="-14" width="56" height="34" rx="16" fill="#B07A50" {s()}/>'
            f'<rect x="-30" y="-24" width="30" height="24" rx="10" fill="#B07A50" {s()}/>'
            f'<ellipse cx="-6" cy="-24" rx="4" ry="3" fill="#8A5530" {W(1.6)}/>'
            + eye(-20, -16, 0.6) + f'<ellipse cx="-28" cy="-8" rx="3" ry="2" fill="{O}"/>'
            + f'<path d="M-26 -2 Q-22 0 -18 -2" fill="none" stroke="{O}" stroke-width="1.6"/>'
            + f'<circle cx="-14" cy="-34" r="8" fill="#FFA53D" {W(2.2)}/><path d="M-14 -42 l3 -4" stroke="#5CB04F" stroke-width="3"/>')


def manta():
    return (f'<path d="M0 -18 Q26 -20 46 4 Q26 6 12 18 L2 40 L-2 40 L-12 18 Q-26 6 -46 4 Q-26 -20 0 -18Z" fill="#4E5F86" {s()}/>'
            f'<path d="M-6 -18 L-10 -28 M6 -18 L10 -28" stroke="{O}" stroke-width="5" stroke-linecap="round"/>' + F(0, -4, 9, 0.65))


def narwhal():
    return (whale("#8E9BD8") + f'<path d="M-20 -18 L-42 -46 L-12 -22Z" fill="#FFF3D6" {W(2.2)}/>'
            f'<path d="M-24 -26 L-17 -24 M-31 -35 L-25 -34" stroke="{O}" stroke-width="1.6"/>')


def moray():   # мурена: длинная, изгибается S-образно, большая голова с улыбкой
    return (f'<path d="M-34 34 Q-40 10 -20 6 Q0 2 -4 -14 Q-6 -28 10 -30 Q30 -32 34 -16 Q36 -4 24 -2 Q14 0 14 -10" fill="none" stroke="{O}" stroke-width="20" stroke-linecap="round"/>'
            f'<path d="M-34 34 Q-40 10 -20 6 Q0 2 -4 -14 Q-6 -28 10 -30 Q30 -32 34 -16 Q36 -4 24 -2 Q14 0 14 -10" fill="none" stroke="#7CBF5A" stroke-width="14" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#4E8A40"/>' for x, y in [(-30, 20), (-16, 6), (-4, -8), (2, -24)])
            + f'<circle cx="22" cy="-22" r="14" fill="#7CBF5A" {s()}/>' + eye(18, -26, 0.6) + eye(28, -24, 0.6)
            + f'<path d="M14 -16 Q23 -4 32 -15Z" fill="#B03A50" {W(2.2)}/><path d="M17 -15 l2 3 l2 -3 l2 3 l2 -3 l2 3 l2 -3" fill="#fff" stroke="{O}" stroke-width="1"/><ellipse cx="12" cy="-20" rx="3" ry="2" fill="{PINK}" opacity=".7"/>')

def sealion():
    return (f'<path d="M-12 30 Q-18 0 -8 -10 L10 -10 Q18 0 14 30Z" fill="#B07A50" {s()}/>'
            f'<ellipse cx="0" cy="-16" rx="16" ry="14" fill="#B07A50" {s()}/><ellipse cx="0" cy="-10" rx="9" ry="6" fill="#D9A97E" {W(1.6)}/>'
            + eye(-7, -20, 0.6) + eye(7, -20, 0.6) + f'<ellipse cx="0" cy="-13" rx="3" ry="2" fill="{O}"/>'
            + f'<path d="M-12 18 L-26 26 L-12 26Z M12 18 L26 26 L12 26Z" fill="#B07A50" {W(2)}/>')


def kid(cap="#FF5A8A", skin="#FFD9B8", pose="float"):
    head = (f'<circle cx="0" cy="0" r="17" fill="{skin}" {s()}/>'
            f'<path d="M-17 -2 Q-17 -19 0 -19 Q17 -19 17 -2Z" fill="{cap}" {s()}/>'
            f'<rect x="-15" y="-4" width="30" height="7" rx="3.5" fill="#3B3355"/><circle cx="-7" cy="-0.5" r="4.5" fill="#9ED3FF" {W(1.6)}/><circle cx="7" cy="-0.5" r="4.5" fill="#9ED3FF" {W(1.6)}/>'
            f'<path d="M-5 9 Q0 13 5 9" fill="none" {W(2)}/>' + cheeks(0, 7, 10))
    if pose == "arms":
        return (f'<path d="M-14 8 L-28 -18 M14 8 L28 -18" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
                f'<path d="M-14 8 L-28 -18 M14 8 L28 -18" stroke="{skin}" stroke-width="5" stroke-linecap="round"/>' + head)
    if pose == "dive":
        return (f'<path d="M0 14 L0 40 M0 24 L-10 44 M0 24 L10 44" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
                f'<path d="M0 14 L0 40" stroke="#3E9BE0" stroke-width="5" stroke-linecap="round"/>'
                f'<path d="M-6 -16 L0 -36 L6 -16" fill="none" stroke="{O}" stroke-width="8" stroke-linecap="round"/>'
                f'<path d="M-6 -16 L0 -36 L6 -16" fill="none" stroke="{skin}" stroke-width="4" stroke-linecap="round"/>' + head)
    return head


HERO = dict(whale=whale, dolphin=dolphin, orca=orca, seal=seal, walrus=walrus, otter=otter, penguin=penguin, turtle=turtle,
            octopus=octopus, clownfish=clownfish, crab=crab, seahorse=seahorse, jelly=jelly, starfish=starfish, puffer=puffer,
            frog=frog, hippo=hippo, polarbear=polarbear, axolotl=axolotl, platypus=platypus, goldfish=goldfish, shark=shark,
            beluga=beluga, capybara=capybara, manta=manta, narwhal=narwhal, moray=moray, sealion=sealion,
            kid=lambda: kid(), kidgirl=lambda: kid("#A98BF0", "#F2C9A0", "arms"), kiddive=lambda: kid("#7CD26E", "#FFD9B8", "dive"))
HERO_RU = dict(whale="китёнок", dolphin="дельфин", orca="косатка", seal="тюлень", walrus="морж", otter="калан", penguin="пингвинёнок",
               turtle="черепашка", octopus="осьминожка", clownfish="рыбка-клоун", crab="крабик", seahorse="морской конёк",
               jelly="медуза", starfish="морская звезда", puffer="рыба-фугу", frog="лягушонок", hippo="бегемотик",
               polarbear="белый медвежонок", axolotl="аксолотль", platypus="утконос", goldfish="золотая рыбка", shark="добрая акула",
               beluga="белуха", capybara="капибара с мандаринкой", manta="скат-манта", narwhal="нарвал", moray="мурена",
               sealion="морской лев", kid="малыш в шапочке и очках", kidgirl="девочка в очках для плавания", kiddive="малыш-ныряльщик")


def put(h, x, y, k=1.0, rot=0, flip=False):
    sx = -k if flip else k
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sx} {k})">{HERO[h]()}</g>'


# =====================  МЕСТА / ДЕЙСТВИЯ  =====================
def surface(y=84, c=BL):
    return f'<path d="M0 {y} Q16 {y-7} 32 {y} T64 {y} T96 {y} T128 {y} V128 H0Z" fill="{c}" {W(2.6)}/>'


def bubbles(pts):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" fill-opacity=".55" {W(1.6)}/>' for x, y, r in pts)


def splash(x, y, k=1.0):
    return "".join(f'<path d="M{x} {y} Q{x+dx*0.5*k} {y-dy*k} {x+dx*k} {y-dy*0.6*k}" fill="none" stroke="#fff" stroke-width="{4*k}" stroke-linecap="round"/>'
                   for dx, dy in [(-22, 18), (-12, 26), (0, 30), (12, 26), (22, 18)]) + "".join(
        f'<circle cx="{x+dx*k}" cy="{y-dy*k}" r="{2.6*k}" fill="#fff"/>' for dx, dy in [(-26, 26), (26, 26), (-8, 36), (10, 38)])


def ring(x, y, rx, ry, c="#E8554A", c2="#fff"):
    segs = "".join(f'<path d="M{x+rx*math.cos(a):.1f} {y+ry*math.sin(a):.1f} A{rx} {ry} 0 0 1 {x+rx*math.cos(a+math.pi/4):.1f} {y+ry*math.sin(a+math.pi/4):.1f}" fill="none" stroke="{c2 if i % 2 else c}" stroke-width="{ry*0.55:.1f}"/>'
                   for i, a in enumerate([j * math.pi / 4 for j in range(8)]))
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx+ry*0.3}" ry="{ry*1.3}" fill="none" stroke="{O}" stroke-width="{ry*0.55+5:.1f}"/>' + segs)


def S_diving(h, v):        # вышка: герой на краю доски или в прыжке
    board = (f'<path d="M6 128 V60" stroke="{O}" stroke-width="9"/><path d="M6 128 V60" stroke="#C0C4D0" stroke-width="5"/>'
             f'<rect x="2" y="56" width="70" height="9" rx="4.5" fill="#3E9BE0" {W(2.4)}/>')
    if v % 2 == 0:
        return board + surface(106) + put(h, 44, 34, 0.85) + splash(104, 106, 0.6)
    return board + surface(106) + put(h, 88, 70, 0.8, rot=60) + f'<path d="M58 30 Q76 26 84 44" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="3 5"/>'


def S_slide(h, v):         # водная горка
    sl = (f'<path d="M4 20 Q60 20 70 60 Q78 92 124 96 V112 Q70 110 58 66 Q50 34 4 36Z" fill="#FFC93C" {s()}/>'
          f'<path d="M8 28 Q58 28 64 62 Q72 100 124 104" fill="none" stroke="{FOAM}" stroke-width="4"/>')
    return sl + surface(108) + put(h, 54 if v % 2 == 0 else 86, 42 if v % 2 == 0 else 80, 0.75, rot=40 if v % 2 == 0 else 10) + bubbles([(110, 96, 4), (118, 86, 3)])


def S_under(h, v):         # подводный мир: плитка дна, пузыри, водоросли
    floor = "".join(f'<rect x="{x}" y="108" width="16" height="20" fill="{c}" stroke="#9ED3FF" stroke-width="1.5"/>' for x, c in zip(range(0, 128, 16), ["#E6F6FF", "#CFEFFF"] * 4))
    weed = f'<path d="M{18 if v else 108} 110 Q{10 if v else 116} 90 {20 if v else 106} 76 Q{28 if v else 98} 64 {20 if v else 108} 52" fill="none" stroke="#5CB04F" stroke-width="6" stroke-linecap="round"/>'
    return (f'<rect x="0" y="0" width="128" height="128" fill="#6CC0F2"/>' + floor + weed
            + put(h, 62, 62, 1.05 if v % 2 == 0 else 0.95, rot=-12 if v else 0, flip=bool(v)) + bubbles([(30, 30, 5), (40, 18, 3), (98, 24, 6), (106, 40, 3)]))


def S_ring(h, v):          # плывёт в надувном круге (вид сверху)
    cols = [("#E8554A", "#fff"), ("#FFC93C", "#FF8A3D"), ("#7CD26E", "#fff"), ("#A98BF0", "#FFD25E")][v % 4]
    return (f'<rect width="128" height="128" fill="{BL}" opacity=".85"/>'
            + "".join(f'<path d="M{x} {y} q8 -5 16 0" fill="none" stroke="{FOAM}" stroke-width="3" stroke-linecap="round"/>' for x, y in [(12, 20), (90, 16), (14, 108), (96, 110)])
            + ring(64, 84, 42, 15, *cols) + put(h, 64, 62, 0.95))


def S_floe(h, v):          # льдина
    return (surface(92, "#7CC8F5") + f'<path d="M14 90 L30 74 L98 72 L116 90 L100 100 L26 100Z" fill="#F4FBFF" {s()}/>'
            f'<path d="M30 74 L40 82 L98 72" fill="none" stroke="#BFE6FF" stroke-width="3"/>' + put(h, 62, 50, 0.95, flip=bool(v % 2)) + sparkle(108, 24, 7))


def S_lily(h, v):          # кувшинка на пруду
    return (f'<rect width="128" height="128" fill="#7CC8F5" opacity=".6"/>'
            f'<path d="M64 96 m-44 0 a44 16 0 1 0 88 0 a44 16 0 1 0 -88 0Z" fill="#7CD26E" {s()}/><path d="M64 96 L100 90" {W(2.6)}/>'
            f'<g transform="translate(26 40)">' + "".join(f'<ellipse cx="0" cy="-8" rx="5" ry="10" fill="#FFB3CF" {W(1.6)} transform="rotate({a})"/>' for a in range(0, 360, 60)) + f'<circle r="5" fill="#FFD25E" {W(1.6)}/></g>'
            + put(h, 70, 64, 0.95))


def S_bowl(h, v):          # аквариум-шар
    return (f'<path d="M30 20 H98 Q120 50 108 92 Q96 116 64 116 Q32 116 20 92 Q8 50 30 20Z" fill="#CFEFFF" fill-opacity=".9" {s()}/>'
            f'<path d="M22 54 H106 Q112 76 104 94 Q92 112 64 112 Q36 112 24 94 Q16 76 22 54Z" fill="{BL}" fill-opacity=".8"/>'
            f'<path d="M30 20 H98" {W(5)}/><path d="M34 32 Q30 46 34 60" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>'
            + put(h, 66, 80, 0.82, flip=bool(v % 2)) + bubbles([(82, 50, 3), (88, 40, 2.5)]))


def S_podium(h, v):        # пьедестал «1»
    return (f'<rect x="38" y="78" width="52" height="46" fill="#FFC93C" {s()}/><rect x="6" y="94" width="34" height="30" fill="#C0C4D0" {s()}/>'
            f'<rect x="88" y="102" width="34" height="22" fill="#E0A870" {s()}/>'
            f'<text x="64" y="112" font-family="Arial Black,Arial" font-weight="900" font-size="26" text-anchor="middle" fill="{O}">1</text>'
            + put(h, 64, 46, 0.92) + f'<circle cx="{88 if v % 2 else 40}" cy="26" r="9" fill="#FFC93C" {W(2.4)}/>' + sparkle(100, 16, 6))


def S_fountain(h, v):      # фонтан/водопад
    return (surface(100) + "".join(f'<path d="M64 100 Q{64+dx} 30 {64+dx*2} {70}" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                                    f'<path d="M64 100 Q{64+dx} 30 {64+dx*2} {70}" fill="none" stroke="#9ED3FF" stroke-width="2" stroke-linecap="round"/>' for dx in (-24, -10, 10, 24))
            + put(h, 64, 40, 0.78) + bubbles([(30, 96, 3), (100, 94, 4)]))


def S_hoop(h, v):          # прыжок через обруч
    return (surface(100) + f'<ellipse cx="66" cy="48" rx="30" ry="34" fill="none" stroke="{O}" stroke-width="10"/><ellipse cx="66" cy="48" rx="30" ry="34" fill="none" stroke="#FF8A3D" stroke-width="6"/>'
            + put(h, 66, 48, 0.75, rot=-25) + splash(22, 100, 0.5))


def S_ball(h, v):          # мяч на носу / пляжный мяч
    ball = (f'<circle cx="0" cy="0" r="15" fill="#fff" {s()}/><path d="M0 -15 A15 15 0 0 1 15 0 L0 0Z" fill="#E8554A"/>'
            f'<path d="M0 15 A15 15 0 0 1 -15 0 L0 0Z" fill="#3E9BE0"/><path d="M15 0 A15 15 0 0 1 0 15 L0 0Z" fill="#FFC93C"/><circle r="15" fill="none" {W(3)}/>')
    return (surface(100) + put(h, 60, 74, 1.05) + f'<g transform="translate({76 if v else 46} 26)">{ball}</g>'
            + f'<path d="M{70 if v else 52} 44 l-4 6 M{84 if v else 40} 44 l4 6" {W(2)}/>')


def S_mattress(h, v):      # дремлет на надувном матрасе
    return (f'<rect width="128" height="128" fill="{BL}" opacity=".8"/>'
            f'<rect x="10" y="70" width="108" height="30" rx="14" fill="{["#FF7FA8", "#7CD26E", "#FFC93C"][v % 3]}" {s()}/>'
            + "".join(f'<path d="M{x} 72 V98" stroke="#fff" stroke-width="3" opacity=".7"/>' for x in (36, 56, 76, 96))
            + put(h, 62, 58, 0.92) + f'<text x="100" y="40" font-family="Arial" font-weight="700" font-size="16" fill="#fff" stroke="{O}" stroke-width="1">z</text>'
            f'<text x="110" y="26" font-family="Arial" font-weight="700" font-size="12" fill="#fff" stroke="{O}" stroke-width="1">z</text>')


def S_kickboard(h, v):     # плывёт с доской
    return (surface(78) + f'<rect x="20" y="66" width="56" height="26" rx="12" fill="#FFC93C" {s()}/>'
            + put(h, 86, 72, 0.9, flip=True) + f'<path d="M106 86 q6 -6 12 0 M110 96 q6 -6 12 0" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')


def S_bubble(h, v):        # внутри большого пузыря
    return (f'<circle cx="64" cy="62" r="46" fill="#9ED3FF" fill-opacity=".55" stroke="#fff" stroke-width="5"/>'
            f'<path d="M36 40 Q42 30 54 26" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
            + put(h, 64, 64, 1.0) + bubbles([(110, 104, 5), (18, 104, 4), (112, 18, 3)]))


def S_surf(h, v):          # сёрфит на волне
    return (f'<path d="M0 128 V80 Q30 40 70 44 Q104 48 110 70 Q92 58 80 70 Q70 90 128 96 V128Z" fill="{BL}" {s()}/>'
            f'<path d="M70 44 Q100 46 110 70" fill="none" stroke="#fff" stroke-width="5"/>'
            f'<ellipse cx="54" cy="76" rx="34" ry="7" fill="#FF8A3D" {W(2.6)} transform="rotate(-12 54 76)"/>' + put(h, 54, 48, 0.8, rot=-8))


def S_ladder(h, v):        # вылезает по лесенке
    return (surface(70) + f'<path d="M86 128 V30 Q86 18 98 18 Q110 18 110 30 M106 128 V30 Q106 26 110 26" fill="none" stroke="{O}" stroke-width="9"/>'
            f'<path d="M86 128 V30 Q86 18 98 18 Q110 18 110 30" fill="none" stroke="#C0C4D0" stroke-width="5"/>'
            + "".join(f'<path d="M86 {y} H106" stroke="{O}" stroke-width="6"/>' for y in (60, 84, 108)) + put(h, 50, 64, 1.0))


def S_block(h, v):         # стартовая тумба
    return (surface(100) + f'<path d="M30 70 H98 L92 100 H36Z" fill="#fff" {s()}/>'
            f'<text x="64" y="94" font-family="Arial Black,Arial" font-weight="900" font-size="20" text-anchor="middle" fill="#3E9BE0">{v % 8 + 1}</text>'
            + put(h, 64, 42, 0.88, rot=-10))


def S_shower(h, v):        # под душем перед бассейном
    return (f'<path d="M20 128 V18 H66" fill="none" stroke="{O}" stroke-width="9"/><path d="M20 128 V18 H66" fill="none" stroke="#C0C4D0" stroke-width="5"/>'
            f'<path d="M52 18 H82 L76 30 H58Z" fill="#C0C4D0" {W(2.6)}/>'
            + "".join(f'<path d="M{x} 38 L{x-2} 48" stroke="#5CB7F2" stroke-width="3" stroke-linecap="round"/>' for x in (58, 66, 74, 62, 70))
            + put(h, 66, 80, 1.0) + bubbles([(98, 70, 5), (108, 56, 3), (96, 48, 4)]))


def S_ripple(h, v):        # вид сверху: круги на воде
    return (f'<rect width="128" height="128" fill="{BL}" opacity=".85"/>'
            + "".join(f'<ellipse cx="64" cy="66" rx="{r}" ry="{r*0.8}" fill="none" stroke="#fff" stroke-width="3" opacity="{1-r/70:.2f}"/>' for r in (30, 42, 54))
            + put(h, 64, 64, 1.05, rot=[0, 30, -30][v % 3]))


def S_umbrella(h, v):      # шезлонг под зонтиком у бассейна
    return (f'<rect x="0" y="96" width="128" height="32" fill="{BL}" {W(2.6)}/>'
            f'<path d="M34 10 L34 96" {W(4)}/><path d="M2 34 Q34 -4 66 34Z" fill="#FF7FA8" {W(2.6)}/><path d="M2 34 Q18 24 34 34 Q50 24 66 34" fill="#fff" {W(2)}/>'
            f'<path d="M30 92 L110 78 L116 88 L36 100Z" fill="#FFC93C" {s()}/>' + put(h, 78, 66, 0.78, rot=-10)
            + f'<path d="M104 52 L100 70 M100 52 H110 L106 58" fill="none" {W(2)}/>')


def S_twin(h, v):          # мама и малыш рядом
    return surface(88) + put(h, 48, 64, 1.0) + put(h, 100, 84, 0.5, flip=True) + f'<path d="M78 46 q-5 -8 -10 -2 q-4 6 10 14 q14 -8 10 -14 q-5 -6 -10 2Z" fill="#FF5A6A" {W(1.8)}/>'


def S_snorkel(h, v):       # маска с трубкой, подглядывает под воду
    return (surface(64) + put(h, 64, 74, 1.05)
            + f'<rect x="44" y="58" width="40" height="18" rx="8" fill="#9ED3FF" fill-opacity=".8" {W(3)}/>'
            f'<path d="M86 68 H92 V24" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/><path d="M86 68 H92 V24" fill="none" stroke="#FF8A3D" stroke-width="5" stroke-linecap="round"/>'
            + bubbles([(98, 18, 4), (104, 10, 3)]))


def S_stars(h, v):         # ночной бассейн со звёздами и подсветкой
    return (f'<rect width="128" height="128" fill="#3B3F7A"/>' + "".join(sparkle(x, y, r, "#FFD25E") for x, y, r in [(22, 20, 5), (100, 16, 6), (110, 44, 4), (16, 50, 3)])
            + f'<path d="M0 84 Q16 77 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="#4FD3E8" {W(2.6)}/>' + put(h, 64, 70, 0.95))


def S_rain(h, v):          # под дождиком из лейки-облака
    return (f'<path d="M30 34 Q30 16 50 18 Q58 6 74 12 Q94 8 96 26 Q110 28 106 40 H32 Q22 40 30 34Z" fill="#fff" {s()}/>'
            + "".join(f'<path d="M{x} 48 l-3 8" stroke="#5CB7F2" stroke-width="3" stroke-linecap="round"/>' for x in (44, 58, 72, 86, 52, 80))
            + surface(100) + put(h, 64, 80, 0.88))


def S_trophy(h, v):        # с кубком
    cup = (f'<path d="M86 30 H118 V44 Q118 64 102 66 Q86 64 86 44Z" fill="#FFC93C" {s()}/><path d="M98 66 V78 H92 V86 H112 V78 H106 V66" fill="#FFC93C" {W(2.6)}/>'
           f'<path d="M86 36 Q76 36 78 46 Q80 54 88 54 M118 36 Q128 36 126 46 Q124 54 116 54" fill="none" {W(2.6)}/>')
    return surface(104) + cup + put(h, 46, 68, 1.0) + sparkle(18, 22, 6) + sparkle(70, 18, 5)


SCENES = dict(diving=S_diving, slide=S_slide, under=S_under, ring=S_ring, floe=S_floe, lily=S_lily, bowl=S_bowl,
              podium=S_podium, fountain=S_fountain, hoop=S_hoop, ball=S_ball, mattress=S_mattress, kickboard=S_kickboard,
              bubble=S_bubble, surf=S_surf, ladder=S_ladder, block=S_block, shower=S_shower, ripple=S_ripple,
              umbrella=S_umbrella, twin=S_twin, snorkel=S_snorkel, stars=S_stars, rain=S_rain, trophy=S_trophy)
SCENE_RU = dict(diving="прыгает с вышки", slide="катится с водной горки", under="плавает под водой среди пузырей",
                ring="плывёт в надувном круге", floe="на льдине", lily="на кувшинке", bowl="в аквариуме-шаре",
                podium="на пьедестале «1» с медалью", fountain="на струях фонтана", hoop="прыгает через обруч",
                ball="играет с пляжным мячом", mattress="дремлет на надувном матрасе", kickboard="плывёт с доской для плавания",
                bubble="внутри большого пузыря", surf="на сёрфе по волне", ladder="у лесенки бассейна",
                block="на стартовой тумбе", shower="под душем у бассейна", ripple="кругами по воде (вид сверху)",
                umbrella="на шезлонге под зонтиком", twin="мама и малыш плывут рядом", snorkel="в маске с трубкой",
                stars="в ночном бассейне под звёздами", rain="под дождиком из облачка", trophy="с кубком чемпиона")
# какие герои естественно смотрятся в каком месте (чтобы не было чепухи вроде «краб на сёрфе вверх ногами»)
FIT = {
    "diving": ["kiddive", "penguin", "frog", "seal", "otter", "polarbear", "capybara", "walrus", "hippo"],
    "slide": ["penguin", "kid", "otter", "seal", "frog", "axolotl", "capybara", "polarbear"],
    "under": ["clownfish", "octopus", "turtle", "manta", "seahorse", "jelly", "puffer", "shark", "goldfish", "moray", "dolphin", "kiddive", "crab", "whale"],
    "ring": ["otter", "capybara", "frog", "penguin", "kid", "seal", "hippo", "polarbear", "axolotl", "whale", "moray"],
    "floe": ["penguin", "polarbear", "seal", "walrus", "beluga", "narwhal"],
    "lily": ["frog", "axolotl", "platypus", "starfish", "crab", "turtle"],
    "bowl": ["goldfish", "clownfish", "axolotl", "puffer", "seahorse", "octopus", "moray"],
    "podium": ["dolphin", "seal", "penguin", "kidgirl", "walrus", "frog", "otter", "sealion", "crab", "moray", "clownfish", "whale"],
    "fountain": ["whale", "beluga", "orca", "dolphin", "narwhal", "seahorse", "clownfish", "moray"],
    "hoop": ["dolphin", "orca", "sealion", "seal", "manta", "kiddive", "moray", "clownfish"],
    "ball": ["sealion", "seal", "walrus", "penguin", "otter", "polarbear", "hippo"],
    "mattress": ["capybara", "otter", "hippo", "walrus", "polarbear", "starfish", "platypus", "seal", "whale"],
    "kickboard": ["kid", "turtle", "frog", "otter", "penguin", "platypus", "axolotl"],
    "bubble": ["jelly", "clownfish", "axolotl", "goldfish", "seahorse", "puffer", "starfish", "octopus", "moray", "whale"],
    "surf": ["seal", "penguin", "otter", "frog", "capybara", "kidgirl", "polarbear", "sealion"],
    "ladder": ["octopus", "crab", "frog", "kidgirl", "platypus", "turtle", "walrus", "moray"],
    "block": ["kiddive", "penguin", "frog", "seal", "otter", "sealion", "polarbear", "hippo"],
    "shower": ["hippo", "penguin", "kidgirl", "otter", "capybara", "polarbear", "frog"],
    "ripple": ["turtle", "manta", "otter", "starfish", "octopus", "frog", "platypus", "shark", "moray", "whale"],
    "umbrella": ["walrus", "crab", "capybara", "seal", "hippo", "penguin", "polarbear", "frog"],
    "twin": ["whale", "beluga", "orca", "dolphin", "seal", "walrus", "manta", "turtle", "narwhal", "moray", "clownfish"],
    "snorkel": ["kid", "frog", "otter", "hippo", "polarbear", "seal", "penguin", "capybara", "whale"],
    "stars": ["whale", "jelly", "narwhal", "manta", "octopus", "beluga", "orca", "moray", "clownfish"],
    "rain": ["frog", "platypus", "penguin", "hippo", "capybara", "otter", "axolotl", "kidgirl", "moray", "whale"],
    "trophy": ["kidgirl", "octopus", "crab", "seal", "dolphin", "walrus", "frog", "sealion", "penguin", "moray", "clownfish", "whale"],
}
BGS = ["sky", "teal", "yellow", "pink", "purple", "orange", "green", "blue"]
# по названию — особенно подходящая сцена
PREF = {"kitenok": ("whale", None), "kashalot": ("whale", "fountain"), "chaika": ("penguin", "surf"), "flamingo": ("frog", "ring"),
        "manta": ("manta", "under"), "delfin": ("dolphin", "hoop"), "aqua-nemo": ("clownfish", None),
        "malysh-i-more": ("seal", "twin"), "mama-ya-plyvu": (None, "twin"), "aquababy": (None, "ring"), "zhemchuzhina": ("octopus", "bubble"),
        "okeana": ("orca", "stars"), "orbita": ("narwhal", "stars"), "raduzhny": ("frog", "rain"), "fiji": ("turtle", "ripple"),
        "olimp80": ("kidgirl", "podium"), "atlant": ("walrus", "trophy"), "zorky": ("seal", "snorkel"), "volna": ("seal", "surf"),
        "morelax": ("capybara", "mattress"), "grebnoy": ("kid", "kickboard"), "arkhimed": ("hippo", "bubble"), "splash": ("kiddive", "diving"),
        "kidswim": ("kid", "ring"), "pool-zil": ("polarbear", "slide"), "formula": ("kiddive", "block"), "bassein": ("capybara", "umbrella")}


def plan():
    places = [p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"] if "pools" in p["cats"]]
    bundled = set(json.load(open(os.path.join(ROOT, "tools", "bundled_icons.json"))))
    used_pair, scene_n, hero_n, todo = set(), {}, {}, []
    rnd = random.Random(7)
    order = list(SCENES)
    for i, p in enumerate(places):
        pid = p["id"]
        ph, ps = next((v for k, v in PREF.items() if k in pid), (None, None))
        best = None
        cands = []
        for sc in ([ps] if ps else []) + rnd.sample(order, len(order)):
            for h in ([ph] if ph else []) + rnd.sample(FIT[sc], len(FIT[sc])):
                if h not in FIT[sc] and h != ph: continue
                if (sc, h) in used_pair: continue
                if hero_n.get(h, 0) >= (2 if h == "moray" else 5): continue   # Вадим: «мурены слишком одинаковые»
                cost = scene_n.get(sc, 0) * 3 + hero_n.get(h, 0) * 2 - (6 if h == ph else 0) - (6 if sc == ps else 0)
                cands.append((cost, sc, h))
        cost, sc, h = min(cands)
        used_pair.add((sc, h)); scene_n[sc] = scene_n.get(sc, 0) + 1; hero_n[h] = hero_n.get(h, 0) + 1
        todo.append(dict(id=pid, name=p["name"], scene=sc, hero=h, v=scene_n[sc] - 1, bg=BGS[(i * 3) % 8], bundled=pid in bundled))
    return todo


if __name__ == "__main__":
    todo = plan()
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for t in todo:
        open(os.path.join(OUT, f"{t['id']}.svg"), "w").write(svg(t["bg"], SCENES[t["scene"]](t["hero"], t["v"])))
        txt = re.sub(rf"^{re.escape(t['id'])} — .*\n", "", txt, flags=re.M) + f"{t['id']} — {HERO_RU[t['hero']]} {SCENE_RU[t['scene']]}\n"
    open(reg, "w").write(txt)
    json.dump([t["id"] for t in todo], open("/tmp/claude-0/pool_ids.json", "w"))
    from collections import Counter
    print(len(todo), "сцен:", Counter(t["scene"] for t in todo).most_common(4), "героев:", Counter(t["hero"] for t in todo).most_common(6))
