"""Иконки робота rare 2026-11-13 (1113h) — каждая придумана и нарисована отдельно (абсолютная уникальность):
- rink-icepark-zhukovsky — герой: красно-белый реактивный самолётик с мордашкой и коньковыми лезвиями вместо шасси | сцена: заходит на «посадку» на голубой лёд крытого катка, оставляя за собой две белые черты (Жуковский — город авиации)
- fk-led-khimki — герой: голубая ледяная буква «Ё» с мордашкой, у которой точки сверху — две снежинки | сцена: скользит на одном белом фигурном коньке, раскинув ручки, по льду школы «ЛЁД»
- squash-sport-lines-ivanteevskaya — герой: чёрный сквош-мячик с двумя жёлтыми точками-глазками на макушке | сцена: шагает, как канатоходец, по красной линии на белой стене корта, держа равновесие ракеткой
Запуск: python3 tools/icons_rare_1113h.py
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")


def save(pid, bg, body):
    open(os.path.join(OUT, pid + ".svg"), "w").write(d.svg(bg, body))


# 1. АйсПарк, Жуковский: самолётик на коньках садится на лёд
def icepark():
    b = ''
    # лёд внизу
    b += '<path d="M0 92 Q64 82 128 92 V128 H0Z" fill="#E8F7FF" ' + d.s('stroke-width="2.6"') + '/>'
    # две белые черты от лезвий
    b += '<path d="M8 104 L56 98 M10 112 L60 106" stroke="#9FD3F0" stroke-width="3" stroke-linecap="round"/>'
    # корпус самолёта (наклон носом вниз-вправо)
    b += '<g transform="rotate(10 70 66)">'
    b += '<path d="M24 64 Q30 50 60 50 L96 52 Q116 56 118 66 Q116 76 96 78 L60 80 Q30 80 24 64Z" fill="#FFFFFF" ' + d.s() + '/>'
    b += '<path d="M28 64 Q34 72 60 74 L96 72" fill="none" stroke="#E8464F" stroke-width="4" stroke-linecap="round"/>'
    # хвост
    b += '<path d="M30 60 L16 34 L30 36 L44 54Z" fill="#E8464F" ' + d.s('stroke-width="2.8"') + '/>'
    # крыло
    b += '<path d="M62 66 L44 92 L58 92 L82 68Z" fill="#E8464F" ' + d.s('stroke-width="2.8"') + '/>'
    # кабина-окошко
    b += '<path d="M100 56 Q110 58 112 64 L100 64Z" fill="#7FC8F2" ' + d.s('stroke-width="2.2"') + '/>'
    b += d.face(84, 62, d=7, k=0.8)
    # стойки и лезвия
    b += '<path d="M58 80 V88 M90 78 V86" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M48 90 H70 Q74 90 74 86 M80 88 H102 Q106 88 106 84" fill="none" stroke="#AEB9CF" stroke-width="4" stroke-linecap="round"/>'
    b += '</g>'
    b += d.sparkle(104, 24, 6, "#FFFFFF") + d.sparkle(18, 84, 4, "#FFFFFF")
    save("rink-icepark-zhukovsky", "sky", b)


# 2. Школа «ЛЁД», Химки: буква Ё на коньке
def led():
    b = ''
    # коньковая дорожка-дуга
    b += '<path d="M14 112 Q64 96 116 108" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity=".8"/>'
    # буква Ё (наклонена — скользит)
    b += '<g transform="rotate(-8 60 64)">'
    b += ('<path d="M42 34 H82 V46 H56 V58 H78 V70 H56 V82 H84 V94 H42Z" fill="#8FD8FF" ' + d.s('stroke-width="3.2"') + '/>'
          '<path d="M46 38 V90" stroke="#D9F3FF" stroke-width="3" stroke-linecap="round"/>')
    b += d.face(68, 64, d=6, k=0.7, blush=True)
    # ручки раскинуты
    b += '<path d="M42 60 Q28 52 20 56 M84 76 Q98 70 106 74" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    # ботинок-конёк под буквой
    b += '<path d="M48 94 L48 104 Q48 108 54 108 L74 108 Q78 108 76 102 L70 94Z" fill="#FFFFFF" ' + d.s('stroke-width="2.6"') + '/>'
    b += '<path d="M44 114 H80 Q84 114 84 110" fill="none" stroke="#AEB9CF" stroke-width="3.4" stroke-linecap="round"/>'
    b += '</g>'

    def flake(x, y, r):
        o = ''
        for i in range(3):
            a = math.radians(i * 60)
            o += f'<path d="M{x - r * math.cos(a):.1f} {y - r * math.sin(a):.1f} L{x + r * math.cos(a):.1f} {y + r * math.sin(a):.1f}" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
        return o
    # точки над Ё — снежинки
    b += flake(52, 20, 7) + flake(74, 17, 7)
    save("fk-led-khimki", "blue", b)


# 3. Пегас, Домодедово: фигурный конёк в балетной пачке под софитом
def pegas():
    b = ''
    b += '<path d="M50 0 L78 0 L110 118 L18 118Z" fill="#FFF6C4" opacity=".55"/>'
    b += '<ellipse cx="64" cy="114" rx="36" ry="6" fill="#FFFFFF" opacity=".7"/>'
    # высокий белый ботинок фигурного конька (голенище вверх, носок вправо)
    b += '<path d="M44 26 Q44 20 50 20 L70 20 Q76 20 76 26 L76 70 Q96 72 100 86 Q100 92 94 92 L46 92 Q42 92 42 86Z" fill="#FFFFFF" ' + d.s() + '/>'
    # шнуровка
    b += '<path d="M62 30 L74 34 M62 40 L74 44 M62 50 L74 54 M62 60 L74 64" stroke="#F58CB8" stroke-width="2.6" stroke-linecap="round"/>'
    # каблук и лезвие с зубцами
    b += '<rect x="46" y="92" width="12" height="6" fill="#C98A4E" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M52 98 V104 M90 92 V104" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<path d="M38 106 H98 Q106 106 104 98 L108 100 L104 104" fill="none" stroke="#9AA6BC" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    # пышная розовая пачка на голенище
    b += '<path d="M22 60 Q30 48 40 54 Q48 42 60 50 Q72 40 82 50 Q96 44 104 56 Q96 68 62 70 Q30 70 22 60Z" fill="#F7A8CC" ' + d.s('stroke-width="2.8"') + '/>'
    b += '<path d="M32 60 Q62 66 94 58" fill="none" stroke="#FFDCEB" stroke-width="2.4" stroke-linecap="round"/>'
    b += d.face(60, 34, d=7, k=0.8)
    b += d.sparkle(22, 28, 6, "#FFFFFF") + d.sparkle(106, 30, 5, "#FFFFFF")
    save("fk-pegas-domodedovo", "purple", b)


# 4. Спортивные линии: мячик-канатоходец на красной линии корта
def lines():
    b = ''
    # белая стена корта
    b += '<rect x="0" y="0" width="128" height="128" fill="#F4F1EA"/>'
    b += '<path d="M0 84 Q64 80 128 84" fill="none" stroke="#E23B3B" stroke-width="6"/>'
    b += '<path d="M0 36 H128" stroke="#E23B3B" stroke-width="3" opacity=".5"/>'
    # мячик
    b += '<circle cx="64" cy="62" r="18" fill="#2B2B33" ' + d.s('stroke-width="3"') + '/>'
    b += '<circle cx="58" cy="46" r="2.8" fill="#FFD43B"/><circle cx="66" cy="45" r="2.8" fill="#FFD43B"/>'
    b += ('<ellipse cx="58" cy="62" rx="3.6" ry="4.4" fill="#FFFFFF"/><ellipse cx="70" cy="62" rx="3.6" ry="4.4" fill="#FFFFFF"/>'
          '<circle cx="58.6" cy="63" r="2" fill="#2B2B33"/><circle cx="70.6" cy="63" r="2" fill="#2B2B33"/>'
          '<path d="M60 70 Q64 73 68 70" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round"/>')
    # ножки на линии
    b += '<path d="M58 79 L56 86 M70 79 L72 86" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    # ракетка-шест для равновесия, длинная, поперёк
    b += '<g transform="rotate(-8 64 56)">'
    b += '<path d="M16 56 H96" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<ellipse cx="106" cy="56" rx="12" ry="9" fill="#FFFFFF" ' + d.s('stroke-width="3"') + '/>'
    b += '<path d="M98 52 H114 M98 56 H114 M98 60 H114 M102 48 V64 M106 47 V65 M110 48 V64" stroke="#9AA3B5" stroke-width="1.2"/>'
    b += '</g>'
    b += '<path d="M46 62 Q34 58 30 56 M82 60 Q90 56 94 54" fill="none" stroke="#3B3355" stroke-width="2.6" stroke-linecap="round"/>'
    save("squash-sport-lines-ivanteevskaya", "yellow", b)


if __name__ == "__main__":
    icepark(); led(); lines()   # «Пегас» не добавлен (нет объекта OSM) — иконка не сохраняется
    print("ok")
