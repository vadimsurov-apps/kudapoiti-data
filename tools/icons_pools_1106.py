"""Бассейны (06.11, Вадим: «аватар не подходит к бассейну», «есть куча морских млекопитающих — подойди творчески»).
Якорь — вода бассейна с дорожкой из поплавков + морской персонаж, плывущий в ней (крупно, по центру, с мордочкой).
У сети — свой герой: «Китёнок» — китёнок, «Мама, я плыву» — мама с малышом (в каждом филиале свой вид),
Aqua Baby — малыш в круге на шее (свой вид), «Немо» — рыбка-клоун, «Кашалотик» — кашалот и т.д.
Шутка — один крупный понятный аксессуар из мира плавания или праздника; пара «персонаж + аксессуар» уникальна."""
import json, math, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O
W = lambda w: s(f'stroke-width="{w}"')
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "icons-src")
F = lambda x, y, d=8, k=0.7, **kw: face(x, y, d=d, k=k, **kw)
BLUE, BLUE2, FOAM = "#5CB7F2", "#3E9BE0", "#BFE6FF"


def water(rope=True):
    """вода бассейна: волна + дорожка поплавков (рисуется ПОВЕРХ тела персонажа, тело «в воде»)"""
    w = (f'<path d="M0 84 Q16 76 32 84 T64 84 T96 84 T128 84 V128 H0Z" fill="{BLUE}" {W(2.6)}/>'
         f'<path d="M10 96 Q20 92 30 96 M84 98 Q94 94 104 98" fill="none" stroke="{FOAM}" stroke-width="3" stroke-linecap="round"/>')
    if rope:
        w += f'<path d="M0 110 H128" stroke="{O}" stroke-width="2"/>' + "".join(
            f'<ellipse cx="{x}" cy="110" rx="6" ry="5" fill="{c}" {W(1.8)}/>' for x, c in zip(range(4, 132, 12), ["#E8554A", "#fff"] * 6))
    return w


# ---------- персонажи: (тело ДО воды, лицо/детали ПОСЛЕ воды, макушка для шапок (x, y), полуширина головы) ----------
def whale(x=64, y=66, k=1.0, col="#4C8EE8"):           # китёнок: круглый, хвост из воды, фонтанчик
    r = 30 * k
    body = (f'<path d="M{x+r*0.6} {y+r*0.5} Q{x+r*1.5} {y+r*0.2} {x+r*1.5} {y-r*0.5} Q{x+r*1.8} {y-r*0.9} {x+r*1.9} {y-r*0.6} '
            f'Q{x+r*1.7} {y-r*0.3} {x+r*1.95} {y-r*0.1} Q{x+r*1.6} {y} {x+r*1.6} {y-r*0.1}" fill="{col}" {W(2.6)}/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{r*1.05}" ry="{r}" fill="{col}" {s()}/>'
            f'<path d="M{x-r*0.8} {y+r*0.35} Q{x} {y+r*0.9} {x+r*0.8} {y+r*0.35} Q{x} {y+r*0.6} {x-r*0.8} {y+r*0.35}Z" fill="#CFE6FF"/>')
    det = F(x - r * 0.15, y - r * 0.05, d=9 * k, k=0.7 * k)
    spout = (f'<path d="M{x} {y-r} V{y-r-12*k} M{x} {y-r-10*k} Q{x-10*k} {y-r-24*k} {x-18*k} {y-r-12*k} M{x} {y-r-10*k} Q{x+10*k} {y-r-24*k} {x+18*k} {y-r-12*k}" '
             f'fill="none" stroke="#fff" stroke-width="{5*k}" stroke-linecap="round"/>'
             f'<path d="M{x} {y-r} V{y-r-12*k} M{x} {y-r-10*k} Q{x-10*k} {y-r-24*k} {x-18*k} {y-r-12*k} M{x} {y-r-10*k} Q{x+10*k} {y-r-24*k} {x+18*k} {y-r-12*k}" '
             f'fill="none" stroke="#7CC8F5" stroke-width="{2*k}" stroke-linecap="round"/>')
    return body, det, (x, y - r + 2), r, spout


def seal(x=64, y=62, k=1.0, col="#9AA7B8"):          # тюлень/нерпа: круглая голова, усы, пятнышки
    r = 27 * k
    body = (f'<ellipse cx="{x}" cy="{y+r*0.9}" rx="{r*1.05}" ry="{r*1.1}" fill="{col}" {s()}/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" {s()}/>'
            + "".join(f'<circle cx="{x+dx*r}" cy="{y+dy*r}" r="{2.2*k}" fill="#7A879A"/>' for dx, dy in [(-.6, -.5), (.5, -.6), (.7, -.2)]))
    det = (F(x, y - r * 0.12, d=9 * k, k=0.6 * k, blush=True)
           + f'<ellipse cx="{x}" cy="{y+r*0.22}" rx="{9*k}" ry="{6*k}" fill="#C9D3DF" {W(1.6)}/><ellipse cx="{x}" cy="{y+r*0.12}" rx="{3.4*k}" ry="{2.4*k}" fill="{O}"/>'
           + "".join(f'<path d="M{x+sg*8*k} {y+r*0.25} L{x+sg*22*k} {y+r*0.25+dy*k}" stroke="{O}" stroke-width="{1.6*k}"/>' for sg in (-1, 1) for dy in (-4, 2)))
    return body, det, (x, y - r + 2), r, ""


def walrus(x=64, y=62, k=1.0):                         # морж: усы, клыки
    b, d, top, r, _ = seal(x, y, k, "#C98A5E")
    d = (F(x, y - r * 0.2, d=9 * k, k=0.55 * k)
         + f'<path d="M{x-6*k} {y+r*0.3} L{x-8*k} {y+r*0.95} L{x-2*k} {y+r*0.35}Z M{x+6*k} {y+r*0.3} L{x+8*k} {y+r*0.95} L{x+2*k} {y+r*0.35}Z" fill="#FFF8E8" {W(1.8)}/>'
         + f'<ellipse cx="{x-7*k}" cy="{y+r*0.2}" rx="{9*k}" ry="{7*k}" fill="#E0B088" {W(1.8)}/><ellipse cx="{x+7*k}" cy="{y+r*0.2}" rx="{9*k}" ry="{7*k}" fill="#E0B088" {W(1.8)}/>'
         + f'<ellipse cx="{x}" cy="{y+r*0.02}" rx="{3.4*k}" ry="{2.4*k}" fill="{O}"/>')
    return b.replace("#7A879A", "#A86F3E"), d, top, r, ""


def otter(x=64, y=62, k=1.0):                          # калан: светлая мордочка, ушки, лапки
    r = 26 * k
    body = (f'<ellipse cx="{x}" cy="{y+r*0.95}" rx="{r*1.05}" ry="{r*1.1}" fill="#A8693E" {s()}/>'
            f'<circle cx="{x-r*0.8}" cy="{y-r*0.65}" r="{6*k}" fill="#A8693E" {W(2.4)}/><circle cx="{x+r*0.8}" cy="{y-r*0.65}" r="{6*k}" fill="#A8693E" {W(2.4)}/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#A8693E" {s()}/>'
            f'<ellipse cx="{x}" cy="{y+r*0.12}" rx="{r*0.78}" ry="{r*0.7}" fill="#F2D3AE"/>')
    det = (F(x, y - r * 0.12, d=8 * k, k=0.6 * k)
           + f'<ellipse cx="{x}" cy="{y+r*0.18}" rx="{4*k}" ry="{3*k}" fill="{O}"/>'
           + f'<ellipse cx="{x-r*0.55}" cy="{y+r*0.95}" rx="{6*k}" ry="{5*k}" fill="#A8693E" {W(2)}/><ellipse cx="{x+r*0.55}" cy="{y+r*0.95}" rx="{6*k}" ry="{5*k}" fill="#A8693E" {W(2)}/>')
    return body, det, (x, y - r + 2), r, ""


def dolphin(x=64, y=58, k=1.0, col="#6FA8DC"):         # дельфин выпрыгивает дугой
    def P(px, py): return f"{x+(px-64)*k:.1f} {y+(py-58)*k:.1f}"
    body = (f'<path d="M{P(30,96)} Q{P(26,50)} {P(62,30)} Q{P(86,20)} {P(104,34)} L{P(116,36)} Q{P(110,44)} {P(100,44)} '
            f'Q{P(80,40)} {P(66,56)} Q{P(52,74)} {P(54,96)}Z" fill="{col}" {s()}/>'
            f'<path d="M{P(62,32)} Q{P(66,14)} {P(80,18)} Q{P(70,26)} {P(72,34)}Z" fill="{col}" {W(2.6)}/>'
            f'<path d="M{P(56,56)} L{P(40,60)} L{P(52,66)}Z" fill="{col}" {W(2.4)}/>'
            f'<path d="M{P(66,54)} Q{P(84,42)} {P(100,44)} Q{P(84,52)} {P(70,64)}Z" fill="#DCEBFA"/>')
    det = (eye(x + 24 * k, y - 20 * k, 0.75 * k)
           + f'<path d="M{P(100,40)} Q{P(106,44)} {P(112,40)}" fill="none" stroke="{O}" stroke-width="{2.2*k}"/>'
           + f'<ellipse cx="{x+18*k}" cy="{y-12*k}" rx="{4*k}" ry="{2.4*k}" fill="#FF7FA8" opacity=".6"/>')
    return body, det, (x + 22 * k, y - 34 * k), 14 * k, ""


def orca(x=64, y=58, k=1.0):                           # косатка: чёрно-белая, глазное пятно
    b, d, top, r, sp = dolphin(x, y, k, "#2E3446")
    b = b.replace('fill="#DCEBFA"', 'fill="#fff"')
    d = (f'<ellipse cx="{x+22*k}" cy="{y-20*k}" rx="{7*k}" ry="{4*k}" fill="#fff" transform="rotate(-20 {x+22*k} {y-20*k})"/>'
         + eye(x + 22 * k, y - 19 * k, 0.65 * k)
         + f'<path d="M{x+36*k} {y-18*k} Q{x+42*k} {y-14*k} {x+48*k} {y-18*k}" fill="none" stroke="#fff" stroke-width="{2.2*k}"/>')
    return b, d, top, r, ""


def manatee(x=64, y=64, k=1.0):                        # ламантин: пухлый, морщинистая мордочка
    r = 29 * k
    body = (f'<ellipse cx="{x}" cy="{y+r*0.7}" rx="{r*1.15}" ry="{r*1.05}" fill="#8FA7A0" {s()}/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.9}" fill="#8FA7A0" {s()}/>'
            f'<ellipse cx="{x}" cy="{y+r*0.32}" rx="{r*0.62}" ry="{r*0.42}" fill="#B9CBC5" {W(2)}/>')
    det = (eye(x - 11 * k, y - r * 0.25, 0.8 * k) + eye(x + 11 * k, y - r * 0.25, 0.8 * k)
           + f'<circle cx="{x-6*k}" cy="{y+r*0.24}" r="{2*k}" fill="{O}"/><circle cx="{x+6*k}" cy="{y+r*0.24}" r="{2*k}" fill="{O}"/>'
           + f'<path d="M{x-8*k} {y+r*0.48} Q{x} {y+r*0.6} {x+8*k} {y+r*0.48}" fill="none" stroke="{O}" stroke-width="{2*k}"/>'
           + f'<ellipse cx="{x-20*k}" cy="{y}" rx="{4*k}" ry="{2.6*k}" fill="#FF7FA8" opacity=".6"/><ellipse cx="{x+20*k}" cy="{y}" rx="{4*k}" ry="{2.6*k}" fill="#FF7FA8" opacity=".6"/>')
    return body, det, (x, y - r * 0.9 + 2), r, ""


def sealion(x=64, y=60, k=1.0):                        # морской лев: вытянутая шея, мяч на носу — нет, просто усатая улыбка
    r = 22 * k
    body = (f'<path d="M{x-r} {y+40*k} Q{x-r*1.1} {y+8*k} {x-r*0.6} {y} L{x+r*0.6} {y} Q{x+r*1.1} {y+8*k} {x+r} {y+40*k}Z" fill="#B07A50" {s()}/>'
            f'<ellipse cx="{x}" cy="{y-6*k}" rx="{r}" ry="{r*0.95}" fill="#B07A50" {s()}/>'
            f'<ellipse cx="{x}" cy="{y+2*k}" rx="{12*k}" ry="{8*k}" fill="#D9A97E" {W(1.8)}/>')
    det = (eye(x - 9 * k, y - 12 * k, 0.75 * k) + eye(x + 9 * k, y - 12 * k, 0.75 * k)
           + f'<ellipse cx="{x}" cy="{y-2*k}" rx="{3.6*k}" ry="{2.6*k}" fill="{O}"/>'
           + f'<path d="M{x-5*k} {y+5*k} Q{x} {y+9*k} {x+5*k} {y+5*k}" fill="none" stroke="{O}" stroke-width="{2*k}"/>'
           + "".join(f'<path d="M{x+sg*10*k} {y+1*k} L{x+sg*22*k} {y+dy*k}" stroke="{O}" stroke-width="{1.4*k}"/>' for sg in (-1, 1) for dy in (-3, 3)))
    return body, det, (x, y - 6 * k - r * 0.95 + 2), r, ""


def narwhal(x=64, y=66, k=1.0):                        # нарвал: китёнок-нарвал с витым рогом
    b, d, top, r, _ = whale(x, y, k, "#8E9BD8")
    horn = (f'<path d="M{x-r*0.55} {y-r*0.75} L{x-r*1.15} {y-r*1.75} L{x-r*0.35} {y-r*0.9}Z" fill="#FFF3D6" {W(2.4)}/>'
            f'<path d="M{x-r*0.62} {y-r*1.0} L{x-r*0.45} {y-r*1.05} M{x-r*0.8} {y-r*1.3} L{x-r*0.66} {y-r*1.33}" stroke="{O}" stroke-width="1.6"/>')
    return b + horn, d, (x + 4 * k, y - r + 2), r, ""


def turtle(x=64, y=64, k=1.0):                         # морская черепаха: голова из воды, панцирь
    r = 30 * k
    body = (f'<ellipse cx="{x}" cy="{y+18*k}" rx="{r*1.2}" ry="{r*0.7}" fill="#6BAE5A" {s()}/>'
            + "".join(f'<path d="M{x+dx*k} {y+6*k} L{x+dx*k} {y+30*k}" stroke="#4E8A40" stroke-width="3"/>' for dx in (-14, 14))
            + f'<path d="M{x-r} {y+16*k} Q{x} {y+4*k} {x+r} {y+16*k}" fill="none" stroke="#4E8A40" stroke-width="3"/>'
            f'<circle cx="{x}" cy="{y-14*k}" r="{20*k}" fill="#A6D98F" {s()}/>')
    det = F(x, y - 13 * k, d=8 * k, k=0.6 * k)
    return body, det, (x, y - 34 * k + 2), 20 * k, ""


def penguin(x=64, y=60, k=1.0):                        # пингвинёнок плывёт
    r = 25 * k
    body = (f'<ellipse cx="{x}" cy="{y+12*k}" rx="{r}" ry="{r*1.25}" fill="#2E3446" {s()}/>'
            f'<ellipse cx="{x}" cy="{y+16*k}" rx="{r*0.72}" ry="{r}" fill="#fff"/>'
            f'<path d="M{x-r*0.7} {y-4*k} Q{x} {y-12*k} {x+r*0.7} {y-4*k} Q{x+r*0.5} {y+12*k} {x} {y+14*k} Q{x-r*0.5} {y+12*k} {x-r*0.7} {y-4*k}Z" fill="#fff"/>')
    det = (eye(x - 8 * k, y + 0 * k, 0.75 * k) + eye(x + 8 * k, y + 0 * k, 0.75 * k)
           + f'<path d="M{x-6*k} {y+8*k} L{x+6*k} {y+8*k} L{x} {y+16*k}Z" fill="#FFB020" {W(2)}/>'
           + f'<ellipse cx="{x-15*k}" cy="{y+8*k}" rx="{4*k}" ry="{2.6*k}" fill="#FF7FA8" opacity=".7"/><ellipse cx="{x+15*k}" cy="{y+8*k}" rx="{4*k}" ry="{2.6*k}" fill="#FF7FA8" opacity=".7"/>')
    return body, det, (x, y + 12 * k - r * 1.25 + 2), r, ""


def octopus(x=64, y=56, k=1.0):                        # осьминожка плещется щупальцами
    r = 27 * k
    body = ("".join(f'<path d="M{x+dx*k} {y+16*k} Q{x+dx*1.6*k} {y+34*k} {x+dx*2.2*k} {y+26*k}" fill="none" stroke="{O}" stroke-width="{12*k}" stroke-linecap="round"/>'
                    f'<path d="M{x+dx*k} {y+16*k} Q{x+dx*1.6*k} {y+34*k} {x+dx*2.2*k} {y+26*k}" fill="none" stroke="#FF8FB1" stroke-width="{7*k}" stroke-linecap="round"/>' for dx in (-20, 20))
            + f'<path d="M{x-r} {y+8*k} Q{x-r} {y-r} {x} {y-r} Q{x+r} {y-r} {x+r} {y+8*k} Q{x+r} {y+22*k} {x} {y+22*k} Q{x-r} {y+22*k} {x-r} {y+8*k}Z" fill="#FF8FB1" {s()}/>'
            + "".join(f'<circle cx="{x+dx*k}" cy="{y+dy*k}" r="{3*k}" fill="#FFC2D6"/>' for dx, dy in [(-14, -14), (12, -18), (16, -6)]))
    det = F(x, y + 2 * k, d=9 * k, k=0.65 * k)
    return body, det, (x, y - r + 2), r, ""


def clownfish(x=64, y=62, k=1.0):                      # рыбка-клоун («Немо»)
    body = (f'<path d="M{x+30*k} {y} L{x+50*k} {y-16*k} Q{x+46*k} {y} {x+50*k} {y+16*k}Z" fill="#FF8A3D" {s()}/>'
            f'<ellipse cx="{x-2*k}" cy="{y}" rx="{36*k}" ry="{26*k}" fill="#FF8A3D" {s()}/>'
            + "".join(f'<path d="M{x+dx*k} {y-25*k} Q{x+(dx+7)*k} {y} {x+dx*k} {y+25*k}" fill="none" stroke="{O}" stroke-width="{10*k}"/>'
                      f'<path d="M{x+dx*k} {y-25*k} Q{x+(dx+7)*k} {y} {x+dx*k} {y+25*k}" fill="none" stroke="#fff" stroke-width="{6*k}"/>' for dx in (-14, 14))
            + f'<path d="M{x-12*k} {y-25*k} Q{x} {y-40*k} {x+14*k} {y-25*k}" fill="#FF8A3D" {W(2.4)}/>')
    det = (eye(x - 24 * k, y - 6 * k, 0.85 * k) + f'<path d="M{x-36*k} {y+6*k} Q{x-30*k} {y+11*k} {x-24*k} {y+6*k}" fill="none" stroke="{O}" stroke-width="{2.4*k}"/>'
           + f'<ellipse cx="{x-30*k}" cy="{y+1*k}" rx="{4*k}" ry="{2.6*k}" fill="#FF5A6A" opacity=".55"/>')
    return body, det, (x + 0 * k, y - 34 * k), 26 * k, ""


def spermwhale(x=64, y=62, k=1.0):                     # кашалот: квадратная голова
    body = (f'<path d="M{x+30*k} {y+12*k} Q{x+52*k} {y+4*k} {x+54*k} {y-14*k} L{x+62*k} {y-20*k} Q{x+58*k} {y-6*k} {x+62*k} {y+2*k} Q{x+50*k} {y+4*k} {x+46*k} {y+14*k}" fill="#7C8AA8" {W(2.6)}/>'
            f'<rect x="{x-38*k}" y="{y-26*k}" width="{72*k}" height="{56*k}" rx="{22*k}" fill="#7C8AA8" {s()}/>'
            f'<path d="M{x-38*k} {y+14*k} H{x+2*k}" stroke="{O}" stroke-width="2.4"/>')
    det = F(x - 14 * k, y - 4 * k, d=9 * k, k=0.65 * k)
    return body, det, (x - 6 * k, y - 26 * k + 2), 30 * k, ""


def gull(x=64, y=58, k=1.0):                           # чайка покачивается на воде
    body = (f'<ellipse cx="{x+4*k}" cy="{y+18*k}" rx="{34*k}" ry="{18*k}" fill="#fff" {s()}/>'
            f'<path d="M{x+4*k} {y+10*k} Q{x+30*k} {y-2*k} {x+44*k} {y+14*k} Q{x+24*k} {y+22*k} {x+4*k} {y+18*k}Z" fill="#B8C4D4" {W(2.4)}/>'
            f'<circle cx="{x-14*k}" cy="{y-6*k}" r="{18*k}" fill="#fff" {s()}/>')
    det = (eye(x - 16 * k, y - 9 * k, 0.75 * k)
           + f'<path d="M{x-30*k} {y-4*k} L{x-46*k} {y} L{x-30*k} {y+3*k}Z" fill="#FFC93C" {W(2.2)}/><circle cx="{x-40*k}" cy="{y+1*k}" r="{2*k}" fill="#E8554A"/>'
           + f'<ellipse cx="{x-8*k}" cy="{y-1*k}" rx="{4*k}" ry="{2.6*k}" fill="#FF7FA8" opacity=".7"/>')
    return body, det, (x - 14 * k, y - 24 * k + 2), 18 * k, ""


def flamingo(x=64, y=56, k=1.0):                       # фламинго в надувном круге
    body = (f'<path d="M{x+6*k} {y+18*k} Q{x+18*k} {y-6*k} {x+2*k} {y-22*k} Q{x-10*k} {y-36*k} {x-22*k} {y-26*k}" fill="none" stroke="{O}" stroke-width="{12*k}" stroke-linecap="round"/>'
            f'<path d="M{x+6*k} {y+18*k} Q{x+18*k} {y-6*k} {x+2*k} {y-22*k} Q{x-10*k} {y-36*k} {x-22*k} {y-26*k}" fill="none" stroke="#FF8FB1" stroke-width="{7*k}" stroke-linecap="round"/>'
            f'<ellipse cx="{x+16*k}" cy="{y+22*k}" rx="{26*k}" ry="{16*k}" fill="#FF8FB1" {s()}/>')
    det = (eye(x - 20 * k, y - 30 * k, 0.6 * k) + f'<path d="M{x-28*k} {y-26*k} Q{x-36*k} {y-22*k} {x-32*k} {y-12*k}" fill="none" stroke="{O}" stroke-width="{5*k}" stroke-linecap="round"/>'
           + f'<path d="M{x-28*k} {y-26*k} Q{x-35*k} {y-22*k} {x-32*k} {y-14*k}" fill="none" stroke="#3B3355" stroke-width="{3*k}" stroke-linecap="round"/>')
    return body, det, (x - 20 * k, y - 38 * k), 12 * k, ""


def manta(x=64, y=62, k=1.0):                          # скат-манта парит над водой
    body = (f'<path d="M{x} {y-20*k} Q{x+28*k} {y-22*k} {x+54*k} {y+4*k} Q{x+30*k} {y+6*k} {x+14*k} {y+20*k} L{x} {y+44*k} L{x-14*k} {y+20*k} '
            f'Q{x-30*k} {y+6*k} {x-54*k} {y+4*k} Q{x-28*k} {y-22*k} {x} {y-20*k}Z" fill="#4E5F86" {s()}/>'
            f'<path d="M{x-8*k} {y-20*k} L{x-12*k} {y-30*k} M{x+8*k} {y-20*k} L{x+12*k} {y-30*k}" stroke="{O}" stroke-width="{5*k}" stroke-linecap="round"/>')
    det = F(x, y - 4 * k, d=10 * k, k=0.7 * k)
    return body, det, (x, y - 30 * k), 20 * k, ""


SPECIES = dict(whale=whale, seal=seal, walrus=walrus, otter=otter, dolphin=dolphin, orca=orca, manatee=manatee,
               sealion=sealion, narwhal=narwhal, turtle=turtle, penguin=penguin, octopus=octopus, clownfish=clownfish,
               spermwhale=spermwhale, gull=gull, flamingo=flamingo, manta=manta)
RU = dict(whale="китёнок", seal="тюлень", walrus="морж", otter="калан", dolphin="дельфин", orca="косатка",
          manatee="ламантин", sealion="морской лев", narwhal="нарвал", turtle="морская черепаха", penguin="пингвинёнок",
          octopus="осьминожка", clownfish="рыбка-клоун", spermwhale="кашалот", gull="чайка", flamingo="фламинго", manta="скат-манта")


# ---------- аксессуары (крупные, из мира плавания и праздника) ----------
def acc(name, top, half):
    cx, t = top
    h = half
    A = {
        "cap": f'<path d="M{cx-h*0.85} {t+h*0.35} Q{cx-h*0.85} {t-h*0.55} {cx} {t-h*0.55} Q{cx+h*0.85} {t-h*0.55} {cx+h*0.85} {t+h*0.35}Z" fill="#FF5A8A" {W(2.6)}/><path d="M{cx-h*0.5} {t-h*0.2} Q{cx} {t-h*0.4} {cx+h*0.5} {t-h*0.2}" stroke="#fff" stroke-width="3" fill="none"/>',
        "goggles": f'<path d="M{cx-h*0.95} {t+h*0.25} H{cx+h*0.95}" stroke="#3B3355" stroke-width="4"/><circle cx="{cx-h*0.38}" cy="{t+h*0.2}" r="{h*0.28}" fill="#9ED3FF" {W(2.4)}/><circle cx="{cx+h*0.38}" cy="{t+h*0.2}" r="{h*0.28}" fill="#9ED3FF" {W(2.4)}/>',
        "crown": f'<path d="M{cx-18} {t+2} L{cx-15} {t-16} L{cx-7} {t-6} L{cx} {t-20} L{cx+7} {t-6} L{cx+15} {t-16} L{cx+18} {t+2}Z" fill="#FFC93C" {W(2.6)}/>',
        "party": f'<path d="M{cx-13} {t+2} L{cx} {t-26} L{cx+13} {t+2}Z" fill="#A98BF0" {W(2.6)}/><circle cx="{cx}" cy="{t-27}" r="4.5" fill="#FFD25E" {W(2)}/>',
        "bow": f'<path d="M{cx} {t-4} L{cx-16} {t-14} V{t+6}Z M{cx} {t-4} L{cx+16} {t-14} V{t+6}Z" fill="#FF5A8A" {W(2.4)}/><circle cx="{cx}" cy="{t-4}" r="4.5" fill="#FF5A8A" {W(2.2)}/>',
        "captain": f'<path d="M{cx-18} {t+2} Q{cx-18} {t-14} {cx} {t-14} Q{cx+18} {t-14} {cx+18} {t+2}Z" fill="#fff" {W(2.6)}/><rect x="{cx-20}" y="{t-1}" width="40" height="7" rx="3" fill="#2E3446" {W(2)}/><circle cx="{cx}" cy="{t-6}" r="3.5" fill="#FFC93C"/>',
        "sailor": f'<path d="M{cx-16} {t+2} Q{cx-16} {t-12} {cx} {t-12} Q{cx+16} {t-12} {cx+16} {t+2}Z" fill="#fff" {W(2.6)}/><rect x="{cx-17}" y="{t-2}" width="34" height="6" fill="#3E9BE0" {W(1.8)}/><path d="M{cx+14} {t+2} L{cx+24} {t+10} M{cx+14} {t+2} L{cx+20} {t+12}" stroke="#3E9BE0" stroke-width="3"/>',
        "medal": f'<path d="M{cx+h+2} {t+h+6} L{cx+h+8} {t+h+20} M{cx+h+18} {t+h+6} L{cx+h+12} {t+h+20}" stroke="#E8554A" stroke-width="4"/><circle cx="{cx+h+10}" cy="{t+h+26}" r="8" fill="#FFC93C" {W(2.4)}/><path d="M{cx+h+10} {t+h+22} V{t+h+30}" {W(2)}/>',
        "whistle": f'<path d="M{cx-h} {t+h*0.9} Q{cx} {t+h*1.5} {cx+h} {t+h*0.9}" fill="none" stroke="#E8554A" stroke-width="3"/><rect x="{cx+h-4}" y="{t+h*0.9}" width="16" height="10" rx="5" fill="#FFC93C" {W(2.2)}/>',
        "balloon": f'<path d="M{min(cx+h, 100)} {t+30} Q{min(cx+h, 100)+6} {t+6} 104 {max(t-4, 30)}" fill="none" {W(2)}/><ellipse cx="104" cy="{max(t-18, 16)}" rx="11" ry="14" fill="#E8554A" {W(2.6)}/>',
        "star": f'<path d="M{cx} {t-26} L{cx+5} {t-14} L{cx+18} {t-13} L{cx+8} {t-5} L{cx+11} {t+7} L{cx} {t} L{cx-11} {t+7} L{cx-8} {t-5} L{cx-18} {t-13} L{cx-5} {t-14}Z" fill="#FFD25E" {W(2.4)}/>',
        "heart": f'<path d="M{cx} {t-2} q-9 -14 -18 -5 q-7 9 18 21 q25 -12 18 -21 q-9 -9 -18 5Z" fill="#FF5A6A" {W(2.2)}/>',
        "flower": f'<g transform="translate({cx+h*0.6} {t+2})">' + "".join(f'<circle cx="{7*math.cos(a):.1f}" cy="{7*math.sin(a):.1f}" r="5.5" fill="#FF7FA8" {W(1.4)}/>' for a in [i * 1.2566 for i in range(5)]) + f'<circle r="4.5" fill="#FFD25E" {W(1.4)}/></g>',
        "lei": "".join(f'<circle cx="{cx-h*0.9+i*h*0.3:.1f}" cy="{t+h*1.5+abs(i-3)*-2:.1f}" r="5" fill="{c}" {W(1.4)}/>' for i, c in enumerate(["#FF7FA8", "#FFD25E", "#FF8A3D", "#FF7FA8", "#FFD25E", "#FF8A3D", "#FF7FA8"])),
        "beanie": f'<path d="M{cx-h*0.8} {t+4} Q{cx-h*0.8} {t-h*0.75} {cx} {t-h*0.75} Q{cx+h*0.8} {t-h*0.75} {cx+h*0.8} {t+4}Z" fill="#3E9BE0" {W(2.6)}/><path d="M{cx-h*0.75} {t-4} H{cx+h*0.75}" stroke="#fff" stroke-width="4"/><circle cx="{cx}" cy="{t-h*0.8}" r="6" fill="#fff" {W(2)}/>',
        "headphones": f'<path d="M{cx-h*0.95} {t+h*0.7} Q{cx-h*0.95} {t-h*0.4} {cx} {t-h*0.4} Q{cx+h*0.95} {t-h*0.4} {cx+h*0.95} {t+h*0.7}" fill="none" {W(4.5)}/><rect x="{cx-h*0.95-7}" y="{t+h*0.45}" width="13" height="18" rx="6" fill="#E8554A" {W(2.2)}/><rect x="{cx+h*0.95-6}" y="{t+h*0.45}" width="13" height="18" rx="6" fill="#E8554A" {W(2.2)}/>',
        "sunglasses": f'<path d="M{cx-h*0.85} {t+h*0.55} H{cx+h*0.85}" {W(3)}/><rect x="{cx-h*0.75}" y="{t+h*0.45}" width="{h*0.6}" height="{h*0.38}" rx="5" fill="#2E3446"/><rect x="{cx+h*0.15}" y="{t+h*0.45}" width="{h*0.6}" height="{h*0.38}" rx="5" fill="#2E3446"/>',
        "graduate": f'<path d="M{cx-22} {t-8} L{cx} {t-18} L{cx+22} {t-8} L{cx} {t+2}Z" fill="#3B3355" {W(2.2)}/><path d="M{cx+20} {t-8} V{t+8}" stroke="#FFC93C" stroke-width="3"/><circle cx="{cx+20}" cy="{t+10}" r="3" fill="#FFC93C"/>',
        "umbrella": f'<path d="M{cx-26} {t-10} Q{cx} {t-40} {cx+26} {t-10}Z" fill="#FFC93C" {W(2.6)}/><path d="M{cx-26} {t-10} Q{cx-13} {t-16} {cx} {t-10} Q{cx+13} {t-16} {cx+26} {t-10}" fill="#E8554A" {W(2)}/><path d="M{cx} {t-10} V{t}" {W(3)}/>',
        "rainbow": "".join(f'<path d="M{cx-34+i*6} {t+2} Q{cx} {t-34+i*6} {cx+34-i*6} {t+2}" fill="none" stroke="{c}" stroke-width="5"/>' for i, c in enumerate(["#E8554A", "#FFC93C", "#7CD26E", "#3E9BE0"])),
        "pirate": f'<path d="M{cx-22} {t+2} Q{cx} {t-26} {cx+22} {t+2} Q{cx} {t-4} {cx-22} {t+2}Z" fill="#3B3355" {W(2.4)}/><circle cx="{cx}" cy="{t-8}" r="3.5" fill="#fff"/>',
        "bunny": f'<ellipse cx="{cx-10}" cy="{t-14}" rx="6" ry="15" fill="#fff" {W(2.4)}/><ellipse cx="{cx+10}" cy="{t-14}" rx="6" ry="15" fill="#fff" {W(2.4)}/><ellipse cx="{cx-10}" cy="{t-14}" rx="2.6" ry="9" fill="#FF7FA8"/><ellipse cx="{cx+10}" cy="{t-14}" rx="2.6" ry="9" fill="#FF7FA8"/>',
        "chef": f'<rect x="{cx-13}" y="{t-8}" width="26" height="10" fill="#fff" {W(2.4)}/><path d="M{cx-13} {t-8} Q{cx-24} {t-18} {cx-12} {t-27} Q{cx} {t-36} {cx+12} {t-27} Q{cx+24} {t-18} {cx+13} {t-8}Z" fill="#fff" {W(2.4)}/>',
        "propeller": f'<path d="M{cx-15} {t+2} Q{cx-15} {t-15} {cx} {t-15} Q{cx+15} {t-15} {cx+15} {t+2}Z" fill="#7CD26E" {W(2.4)}/><path d="M{cx} {t-15} V{t-22}" {W(3)}/><ellipse cx="{cx-9}" cy="{t-24}" rx="9" ry="3.5" fill="#E8554A" {W(1.8)}/><ellipse cx="{cx+9}" cy="{t-24}" rx="9" ry="3.5" fill="#3E9BE0" {W(1.8)}/>',
        "cowboy": f'<ellipse cx="{cx}" cy="{t}" rx="27" ry="6" fill="#C08A5A" {W(2.4)}/><path d="M{cx-14} {t-1} Q{cx-14} {t-22} {cx} {t-17} Q{cx+14} {t-22} {cx+14} {t-1}Z" fill="#C08A5A" {W(2.4)}/>',
        "wreath": "".join(f'<circle cx="{cx+dx}" cy="{t-2+abs(dx)//4}" r="5.5" fill="{c}" {W(1.4)}/>' for dx, c in [(-20, "#FF7FA8"), (-10, "#FFD25E"), (0, "#9ED3FF"), (10, "#FF7FA8"), (20, "#FFD25E")]),
        "santa": f'<path d="M{cx-18} {t+2} Q{cx} {t-28} {cx+22} {t-18} L{cx+18} {t+2}Z" fill="#E8304A" {W(2.4)}/><rect x="{cx-20}" y="{t-4}" width="40" height="9" rx="4.5" fill="#fff" {W(2.2)}/><circle cx="{cx+24}" cy="{t-18}" r="5" fill="#fff" {W(2)}/>',
        "tiara": f'<path d="M{cx-17} {t+2} Q{cx} {t-18} {cx+17} {t+2}" fill="none" stroke="#C0C4D0" stroke-width="5"/><circle cx="{cx}" cy="{t-11}" r="4.5" fill="#9ED3FF" {W(1.8)}/>',
    }
    return A[name]


ACC = ["cap", "goggles", "crown", "party", "bow", "captain", "sailor", "medal", "balloon", "star", "heart", "flower",
       "beanie", "headphones", "sunglasses", "graduate", "umbrella", "rainbow", "pirate", "bunny", "propeller", "cowboy",
       "wreath", "santa", "lei", "chef"]
ACC_RU = dict(cap="в плавательной шапочке", goggles="в очках для плавания", crown="в короне", party="в праздничном колпачке",
              bow="с бантом", captain="в капитанской фуражке", sailor="в бескозырке", medal="с медалью пловца",
              whistle="со свистком тренера", balloon="с воздушным шариком", star="со звездой", heart="с сердечком",
              flower="с цветком", beanie="в шапке с помпоном", headphones="в наушниках", sunglasses="в тёмных очках",
              graduate="в шапке выпускника", umbrella="под пляжным зонтиком", rainbow="под радугой", pirate="в пиратской треуголке",
              bunny="с заячьими ушками", propeller="в кепке с пропеллером", cowboy="в ковбойской шляпе", wreath="в цветочном венке",
              santa="в новогоднем колпаке", tiara="в диадеме", lei="в гавайских бусах", chef="в поварском колпаке")


def neckring(top, half, cy):
    """надувной круг на шее малыша (Aqua Baby)"""
    cx = top[0]
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{half*1.25}" ry="{half*0.42}" fill="#FFC93C" {W(2.6)}/>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{half*0.72}" ry="{half*0.2}" fill="#FF8A3D" {W(2)}/>')


def scene(kind, a=None, mode="single", bg="sky", rope=True):
    """single — персонаж в бассейне; mama — мама и малыш рядом; baby — малыш в круге на шее"""
    fn = SPECIES[kind]
    if mode == "mama":
        b1, d1, t1, h1, x1 = fn(46, 64, 0.9) if kind not in ("dolphin", "orca") else fn(48, 62, 0.82)
        b2, d2, t2, h2, x2 = fn(98, 82, 0.5) if kind not in ("dolphin", "orca") else fn(92, 82, 0.45)
        body = b1 + b2 + water(rope) + d1 + d2 + x1 + x2
        if a: body += acc(a, t1, h1)
        return svg(bg, body)
    b, d, t, h, x = fn()
    body = b + water(rope) + d + x
    if mode == "baby":
        body = b + water(rope) + neckring(t, h, t[1] + h * 1.75 if kind not in ("dolphin", "orca", "clownfish", "manta", "flamingo", "gull") else t[1] + 40) + d + x
    if a:
        body += acc(a, t, h)
    return svg(bg, body)


# ---------- кто кем будет ----------
CHAIN = [("kitenok", "whale", "single"), ("kashalot", "spermwhale", "single"), ("mama-ya-plyvu", None, "mama"),
         ("aquababy", None, "baby"), ("aqua-nemo", "clownfish", "single"), ("detskaya-bukhta", "sealion", "single"),
         ("proplyt", "dolphin", "single"), ("chaika", "gull", "single"), ("flamingo", "flamingo", "single"),
         ("manta", "manta", "single"), ("delfin", "dolphin", "single"), ("morelax", "seal", "single"),
         ("orbita", "narwhal", "single"), ("okeana", "orca", "single"), ("kidswim", "penguin", "single"),
         ("fiji", "turtle", "single"), ("kidway", "octopus", "single"), ("malysh-i-more", "seal", "single"),
         ("more-detyam", "otter", "single"), ("aquapups", "seal", "single"), ("akvaroom", "octopus", "single"),
         ("aqua-class", "otter", "single"), ("atlant", "walrus", "single"), ("volna", "dolphin", "single"),
         ("zorky", "sealion", "single"), ("arkhimed", "turtle", "single"), ("zhemchuzhina", "otter", "single")]
CYCLE = ["seal", "walrus", "otter", "manatee", "sealion", "turtle", "penguin", "narwhal", "octopus", "orca", "dolphin"]
MAMA = ["seal", "walrus", "otter", "manatee", "sealion", "turtle", "penguin", "narwhal", "orca", "dolphin", "octopus"]
BABY = ["seal", "otter", "walrus", "penguin", "manatee", "sealion", "turtle", "narwhal", "octopus", "spermwhale", "whale"]
# подходящая шутка по названию
NAME_ACC = {"pool-atlant": "medal", "fiji-kids": "lei", "pool-zorky": "goggles", "orbita-pool-zelenograd": "star",
            "raduzhny-fok-pool": "rainbow", "zhemchuzhina-pool-mitino": "tiara", "chaika-swim-school": "sailor",
            "olimp80-pool": "medal", "grebnoy-kanal-pool": "captain", "morelax-pool": "sunglasses",
            "malysh-i-more": "sailor", "pool-volna-chertanovo": "goggles", "flamingo-naro-fominsk": "sunglasses",
            "aqua-class-alekseevskaya": "graduate", "aqua-class-rybalko": "cap", "manta-club": "crown",
            "kashalotik-pool": "captain", "okeana-krasnogorsk": "crown", "pool-arkhimed-dubna": "graduate"}
BGS = ["sky", "teal", "yellow", "pink", "purple", "orange", "green", "blue"]
KEEP = ("murena-",)  # мурены уже понятные и смешные


def plan():
    places = [p for p in json.load(open(os.path.join(ROOT, "places-all.json")))["places"] if "pools" in p["cats"]]
    bundled = set(json.load(open(os.path.join(ROOT, "tools", "bundled_icons.json"))))
    todo, used, i_cyc, i_mama, i_baby = [], set(), 0, 0, 0
    for p in places:
        pid = p["id"]
        if pid.startswith(KEEP):
            continue
        sp, mode = None, "single"
        for key, s_, m in CHAIN:
            if key in pid:
                sp, mode = s_, m
                break
        if mode == "mama":
            sp = MAMA[i_mama % len(MAMA)]; i_mama += 1
        elif mode == "baby":
            sp = BABY[i_baby % len(BABY)]; i_baby += 1
        elif not sp:
            sp = CYCLE[i_cyc % len(CYCLE)]; i_cyc += 1
        want = [NAME_ACC[pid]] if pid in NAME_ACC else []
        rot = ACC[len(todo) * 5 % len(ACC):] + ACC[:len(todo) * 5 % len(ACC)]   # разные шутки подряд, а не «шапочка» у всех
        a = next(x for x in want + rot if (sp, mode, x) not in used)
        used.add((sp, mode, a))
        todo.append(dict(id=pid, name=p["name"], sp=sp, mode=mode, acc=a, bg=BGS[len(todo) * 3 % len(BGS)], bundled=pid in bundled))
    return todo


def subject(t):
    who = RU[t["sp"]]
    if t["mode"] == "mama":
        return f"мама-{who} и малыш плывут по дорожке бассейна, {ACC_RU[t['acc']]}"
    if t["mode"] == "baby":
        return f"малыш-{who} в надувном круге на шее в бассейне, {ACC_RU[t['acc']]}"
    return f"{who} плывёт по дорожке бассейна, {ACC_RU[t['acc']]}"


if __name__ == "__main__":
    todo = plan()
    reg = os.path.join(OUT, "subjects.txt"); txt = open(reg).read()
    for t in todo:
        open(os.path.join(OUT, f"{t['id']}.svg"), "w").write(scene(t["sp"], t["acc"], t["mode"], t["bg"]))
        txt = re.sub(rf"^{re.escape(t['id'])} — .*\n", "", txt, flags=re.M) + f"{t['id']} — {subject(t)}\n"
    open(reg, "w").write(txt)
    json.dump([t["id"] for t in todo], open("/tmp/claude-0/pool_ids.json", "w"))
    from collections import Counter
    print(len(todo), Counter(t["sp"] for t in todo), sum(t["bundled"] for t in todo), "встроенных")
