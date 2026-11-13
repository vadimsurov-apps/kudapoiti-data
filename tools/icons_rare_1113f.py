"""Иконки робота rare 2026-11-13 (1113f) — каждая придумана и нарисована отдельно (абсолютная уникальность):
- rink-ms-svyatoozerskaya — герой: зелёная ёлочка на коньках с мордашкой | сцена: катится по льду открытого катка у круглого озера под снегопадом (Святое озеро, Косино)
- volley-plotik-khimki — герой: жёлто-синий волейбольный мяч-гребец | сцена: стоит на бревенчатом плотике среди волн и гребёт веслом (школа «Плотик»)
- rink-olimpiysky-maksimova-chekhov — герой: белый фигурный конёк с золотым лезвием | сцена: стоит на синей тумбе-пьедестале на льду под гирляндой флажков
- rink-armada-odintsovo — герой: бумажный кораблик на коньке-полозе | сцена: скользит по льду во главе двух маленьких корабликов («Армада»)
- rink-arena-morozovo-mass — герой: большой голубой ботинок-конёк с морозным узором | сцена: ведёт за шнурок маленький розовый детский конёк по катку
Запуск: python3 tools/icons_rare_1113f.py
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

O = d.O
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")


def save(pid, bg, body):
    open(os.path.join(OUT, pid + ".svg"), "w").write(d.svg(bg, body))


# 1. Ракетка в вязаном шарфике (ТТ Текстильщики)
def tekstil():
    b = ''
    # ручка (снизу справа), наклон
    b += '<g transform="rotate(-28 64 64)">'
    b += '<rect x="56" y="84" width="16" height="34" rx="6" fill="#C98A4E" ' + d.s('stroke-width="3.0"') + '/>'
    b += '<path d="M60 92 V112 M68 92 V112" stroke="#A86B35" stroke-width="1.8" stroke-linecap="round"/>'
    # круглая красная накладка
    b += '<circle cx="64" cy="54" r="34" fill="#E8464F" ' + d.s('stroke-width="3.4"') + '/>'
    b += '<circle cx="64" cy="54" r="27" fill="none" stroke="#F17A80" stroke-width="2"/>'
    b += d.face(64, 50, d=9, k=1.1)
    b += '</g>'
    # вязаный шарфик на «шее» (у основания накладки), полосатый, конец развевается
    b += ('<path d="M40 82 Q60 92 82 78 L86 88 Q62 102 38 92Z" fill="#5FA9E8" ' + d.s('stroke-width="2.8"') + '/>'
          '<path d="M48 86 L46 95 M58 89 L57 98 M68 87 L69 96 M78 83 L80 92" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>'
          '<path d="M82 82 Q98 84 106 96 L100 102 Q94 92 80 90Z" fill="#5FA9E8" ' + d.s('stroke-width="2.6"') + '/>'
          '<path d="M100 102 l-2 6 M104 99 l2 6" stroke="#3B3355" stroke-width="2" stroke-linecap="round"/>')
    # белый шарик слева сверху с линиями движения
    b += '<circle cx="24" cy="30" r="9" fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M36 22 H46 M36 30 H44" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    save("tt-tekstilshchiki-saratovskaya", "pink", b)


# 2. Шарик-эквилибрист на ребре ракетки (Фортуна)
def fortuna():
    b = ''
    # синяя ракетка лицом к нам, чуть наклонена; ручка вниз
    b += '<g transform="rotate(12 64 80)">'
    b += '<rect x="57" y="98" width="14" height="28" rx="5" fill="#C98A4E" ' + d.s('stroke-width="3.0"') + '/>'
    b += '<circle cx="64" cy="76" r="27" fill="#3E6FD8" ' + d.s('stroke-width="3.4"') + '/>'
    b += '<circle cx="64" cy="76" r="20" fill="none" stroke="#6E95EE" stroke-width="2"/>'
    b += '</g>'
    # оранжевый шарик стоит на верхнем ободе ракетки
    b += '<circle cx="58" cy="32" r="17" fill="#FF9A3C" ' + d.s('stroke-width="3.2"') + '/>'
    b += '<path d="M47 24 Q52 18 58 18" fill="none" stroke="#FFD2A0" stroke-width="3" stroke-linecap="round"/>'
    b += d.face(58, 32, d=6, k=0.8)
    # ручки-балансир в стороны
    b += '<path d="M41 34 Q32 28 26 32 M75 34 Q84 28 90 32" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    # падающие звёздочки удачи
    def star(x, y, r, c):
        pts = []
        for i in range(10):
            a = math.radians(-90 + i * 36)
            rr = r if i % 2 == 0 else r * 0.45
            pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
        return f'<polygon points="{" ".join(pts)}" fill="{c}" ' + d.s('stroke-width="2.0"') + '/>'
    b += star(22, 70, 8, "#FFE45E") + star(106, 66, 7, "#FFE45E") + star(98, 104, 5, "#FFFFFF") + star(28, 104, 5, "#FFFFFF")
    save("tt-fortuna-armavirskaya", "yellow", b)


# 3. Мяч-гребец на плотике (Плотик)
def plotik():
    # волны
    b = ('<path d="M-4 96 Q8 90 20 96 T44 96 T68 96 T92 96 T116 96 T140 96 V132 H-4Z" fill="#4FA8E0"/>'
         '<path d="M-4 108 Q10 102 24 108 T52 108 T80 108 T108 108 T136 108" fill="none" stroke="#BDE3FA" stroke-width="2.6" stroke-linecap="round"/>')
    # плотик из трёх брёвен
    for i, y in enumerate((88, 92, 96)):
        pass
    b += ('<rect x="28" y="84" width="72" height="9" rx="4.5" fill="#C98A4E" ' + d.s('stroke-width="2.6"') + '/>'
          '<rect x="26" y="92" width="76" height="9" rx="4.5" fill="#B5763C" ' + d.s('stroke-width="2.6"') + '/>'
          '<circle cx="31" cy="88.5" r="2.4" fill="#E8C08F"/><circle cx="29" cy="96.5" r="2.4" fill="#E8C08F"/>')
    # весло
    b += ('<path d="M92 34 L104 100" stroke="#8C5A2B" stroke-width="5" stroke-linecap="round"/>'
          '<path d="M100 92 Q110 98 108 112 Q100 112 98 100Z" fill="#E7B987" ' + d.s('stroke-width="2.4"') + '/>')
    # мяч
    b += '<circle cx="62" cy="58" r="27" fill="#FFFFFF" ' + d.s('stroke-width="3.4"') + '/>'
    b += ('<path d="M38 50 Q62 44 84 60" fill="none" stroke="#3E6FD8" stroke-width="7"/>'
          '<path d="M44 76 Q60 62 86 66" fill="none" stroke="#FFD43B" stroke-width="7"/>'
          '<circle cx="62" cy="58" r="27" fill="none" ' + d.s('stroke-width="3.4"') + '/>')
    b += d.face(60, 60, d=8, k=1.0)
    # ручка к веслу
    b += '<path d="M86 62 Q92 56 94 46" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += d.sparkle(20, 30, 5, "#FFFFFF") + d.sparkle(36, 18, 3.5, "#FFFFFF")
    save("volley-plotik-khimki", "sky", b)


# 4. Конёк на пьедестале под флажками (ЛД «Олимпийский», Чехов)
def chekhov():
    b = ('<rect x="-4" y="104" width="136" height="28" fill="#EAF7FF"/>'
         '<path d="M-4 104 H132" stroke="#9FCFE6" stroke-width="2.4"/>')
    # гирлянда флажков сверху
    b += '<path d="M6 22 Q64 42 122 22" fill="none" stroke="#3B3355" stroke-width="2"/>'
    cols = ["#E8464F", "#FFD43B", "#5CCD8A", "#5FA9E8", "#A98BF0", "#FF9A3C"]
    for i, t in enumerate((0.12, 0.27, 0.42, 0.58, 0.73, 0.88)):
        x = 6 + 116 * t
        y = 22 + 20 * 4 * t * (1 - t)
        b += f'<path d="M{x-5:.1f} {y-1:.1f} L{x+5:.1f} {y+1:.1f} L{x:.1f} {y+12:.1f}Z" fill="{cols[i]}" ' + d.s('stroke-width="1.6"') + '/>'
    # пьедестал
    b += '<rect x="38" y="84" width="52" height="22" rx="3" fill="#3E6FD8" ' + d.s('stroke-width="3.0"') + '/>'
    # конёк: ботинок + золотое лезвие
    b += ('<path d="M42 34 Q42 26 52 26 L66 26 Q72 26 72 34 L72 56 Q88 56 92 66 Q94 74 86 74 L42 74Z" '
          'fill="#FFFFFF" ' + d.s('stroke-width="3.2"') + '/>')
    b += '<path d="M50 36 L64 36 M50 43 L64 43 M50 50 L64 50 M50 57 L64 57" stroke="#9FB4D6" stroke-width="2" stroke-linecap="round"/>'
    b += '<path d="M50 74 V80 M84 74 V80" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M40 80 H92 Q96 80 94 84 H42Z" fill="#FFC93C" ' + d.s('stroke-width="2.6"') + '/>'
    b += d.face(78, 66, d=5, k=0.75, blush=False)
    b += d.sparkle(26, 60, 5, "#FFFFFF") + d.sparkle(104, 52, 5, "#FFFFFF")
    save("rink-olimpiysky-maksimova-chekhov", "blue", b)


# 5. Бумажный кораблик-флагман на коньке (ЛД «Армада»)
def armada():
    b = ('<rect x="-4" y="96" width="136" height="36" fill="#EAF7FF"/>'
         '<path d="M-4 96 H132" stroke="#9FCFE6" stroke-width="2.4"/>'
         '<path d="M14 116 Q50 108 96 116" fill="none" stroke="#BBDCF2" stroke-width="2.4" stroke-linecap="round"/>')

    def boat(cx, by, k, col, face=False):
        w = 36 * k
        h = 30 * k
        o = (f'<path d="M{cx-w:.1f} {by-h*0.5:.1f} L{cx+w:.1f} {by-h*0.5:.1f} L{cx+w*0.7:.1f} {by:.1f} L{cx-w*0.7:.1f} {by:.1f}Z" '
             f'fill="{col}" ' + d.s(f'stroke-width="{2.8*k:.1f}"') + '/>'
             f'<path d="M{cx-w*0.55:.1f} {by-h*0.5:.1f} L{cx:.1f} {by-h*1.5:.1f} L{cx+w*0.55:.1f} {by-h*0.5:.1f}Z" '
             f'fill="#FFFFFF" ' + d.s(f'stroke-width="{2.8*k:.1f}"') + '/>'
             f'<path d="M{cx:.1f} {by-h*1.5:.1f} V{by-h*0.5:.1f}" stroke="#C9D3E6" stroke-width="{1.8*k:.1f}"/>'
             # полоз-лезвие
             f'<path d="M{cx-w*0.8:.1f} {by+5*k:.1f} H{cx+w*0.85:.1f} Q{cx+w:.1f} {by+5*k:.1f} {cx+w*0.9:.1f} {by:.1f}" fill="none" stroke="#7F8FAF" stroke-width="{3.2*k:.1f}" stroke-linecap="round"/>'
             f'<path d="M{cx-w*0.4:.1f} {by:.1f} V{by+5*k:.1f} M{cx+w*0.4:.1f} {by:.1f} V{by+5*k:.1f}" stroke="#3B3355" stroke-width="{2.4*k:.1f}"/>')
        if face:
            o += d.face(cx, by - h * 0.25 + 1, d=7 * k, k=0.8 * k, blush=True)
        return o
    b += boat(24, 72, 0.45, "#FFD43B") + boat(46, 80, 0.55, "#FF9A3C")
    b += boat(80, 92, 1.0, "#E8464F", face=True)
    b += d.sparkle(108, 30, 5, "#FFFFFF") + d.sparkle(20, 30, 4, "#FFFFFF")
    save("rink-armada-odintsovo", "teal", b)


# 6. Большой конёк ведёт малыша-конька (Арена «Морозово»)
def morozovo():
    b = ('<rect x="-4" y="104" width="136" height="28" fill="#DDF0FF"/>'
         '<path d="M-4 104 H132" stroke="#9FCFE6" stroke-width="2.4"/>')

    def skate(x, y, k, col, blade="#AEB9CF"):
        o = (f'<path d="M{x:.1f} {y:.1f} Q{x:.1f} {y-8*k:.1f} {x+8*k:.1f} {y-8*k:.1f} L{x+22*k:.1f} {y-8*k:.1f} '
             f'Q{x+28*k:.1f} {y-8*k:.1f} {x+28*k:.1f} {y:.1f} L{x+28*k:.1f} {y+22*k:.1f} Q{x+46*k:.1f} {y+22*k:.1f} {x+50*k:.1f} {y+30*k:.1f} '
             f'Q{x+52*k:.1f} {y+36*k:.1f} {x+46*k:.1f} {y+36*k:.1f} L{x:.1f} {y+36*k:.1f}Z" fill="{col}" ' + d.s(f'stroke-width="{3.2*min(k,1):.1f}"') + '/>'
             f'<path d="M{x+4*k:.1f} {y+36*k:.1f} V{y+42*k:.1f} M{x+42*k:.1f} {y+36*k:.1f} V{y+42*k:.1f}" stroke="#3B3355" stroke-width="{2.8*min(k,1):.1f}"/>'
             f'<path d="M{x-4*k:.1f} {y+42*k:.1f} H{x+50*k:.1f} Q{x+56*k:.1f} {y+42*k:.1f} {x+52*k:.1f} {y+46*k:.1f} H{x-2*k:.1f}Z" fill="{blade}" ' + d.s(f'stroke-width="{2.4*min(k,1):.1f}"') + '/>')
        return o
    # большой голубой конёк
    b += skate(20, 40, 1.15, "#8CCBF5")
    # морозный узор на ботинке
    b += ('<g stroke="#FFFFFF" stroke-width="2" stroke-linecap="round">'
          '<path d="M36 54 V70 M28 62 H44 M30 56 L42 68 M42 56 L30 68"/></g>')
    b += d.face(66, 74, d=6, k=0.85)
    # шнурок к малышу
    b += '<path d="M48 40 Q70 22 92 64" fill="none" stroke="#3B3355" stroke-width="2.2" stroke-dasharray="1 0"/>'
    # маленький розовый конёк
    b += skate(82, 70, 0.55, "#FFB3CF")
    b += d.face(99, 85, d=3.5, k=0.55, blush=False)
    b += d.sparkle(104, 28, 5, "#FFFFFF") + d.sparkle(18, 26, 4, "#FFFFFF")
    save("rink-arena-morozovo-mass", "night", b)


# 7. Ёлочка на коньках у озера (бесплатный каток «Московских сезонов», Святоозёрская ул.)
def svyato():
    b = ('<ellipse cx="100" cy="86" rx="40" ry="9" fill="#7FB8E8" ' + d.s('stroke-width="2.2"') + '/>'
         '<rect x="-4" y="98" width="136" height="34" fill="#EAF7FF"/>'
         '<path d="M-4 98 H132" stroke="#9FCFE6" stroke-width="2.4"/>'
         '<path d="M20 116 Q44 108 70 114" fill="none" stroke="#BBDCF2" stroke-width="2.4" stroke-linecap="round"/>')
    # ёлочка — три яруса, наклонена в движении
    b += '<g transform="rotate(-8 56 70)">'
    b += '<path d="M56 16 L82 50 H30Z" fill="#3FA36B" ' + d.s('stroke-width="3.0"') + '/>'
    b += '<path d="M56 32 L88 70 H24Z" fill="#3FA36B" ' + d.s('stroke-width="3.0"') + '/>'
    b += '<path d="M56 50 L94 90 H18Z" fill="#3FA36B" ' + d.s('stroke-width="3.0"') + '/>'
    b += '<path d="M36 64 Q56 72 76 62 M30 84 Q56 92 84 82" fill="none" stroke="#2C7F52" stroke-width="2.2" stroke-linecap="round"/>'
    b += d.face(56, 70, d=7, k=0.9)
    # ножки и два конька
    b += '<path d="M46 90 V96 M66 90 V96" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M38 96 H54 Q58 96 56 100 H40Z M58 96 H74 Q78 96 76 100 H60Z" fill="#E8464F" ' + d.s('stroke-width="2.4"') + '/>'
    b += '<path d="M36 103 H58 M56 103 H80" stroke="#7F8FAF" stroke-width="3" stroke-linecap="round"/>'
    b += '</g>'
    # снежинки-снегопад
    for x, y, r in ((100, 22, 3), (114, 44, 2.5), (92, 52, 2), (16, 30, 2.5), (26, 52, 2)):
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF"/>'
    save("rink-ms-svyatoozerskaya", "sky", b)


if __name__ == "__main__":
    svyato(); plotik(); chekhov(); armada(); morozovo()
    print("ok")
