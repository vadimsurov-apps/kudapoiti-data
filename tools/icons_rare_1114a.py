"""Иконки робота rare 2026-11-14 (1114a) — каждая придумана и нарисована отдельно (абсолютная уникальность).
Реестр строк — в SUBJ ниже (дописываются в icons-src/subjects.txt). Запуск: python3 tools/icons_rare_1114a.py
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import draw_icons as d

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src")
SUBJ = {}


def save(pid, bg, body, hero, scene):
    open(os.path.join(OUT, pid + ".svg"), "w").write(d.svg(bg, body))
    SUBJ[pid] = f"{pid} — герой: {hero} | сцена: {scene}"


def blade(x1, x2, y, col="#AEB9CF"):
    return f'<path d="M{x1} {y} H{x2} Q{x2 + 6} {y} {x2 + 6} {y - 5}" fill="none" stroke="{col}" stroke-width="4.5" stroke-linecap="round"/>'


# 1. Мастера хоккея (Мосфильмовская): тренерский планшет с хоккейной площадкой
def masters():
    b = ''
    # планшет
    b += '<rect x="22" y="26" width="76" height="86" rx="10" fill="#FFFFFF" ' + d.s() + '/>'
    b += '<rect x="46" y="18" width="28" height="14" rx="4" fill="#9AA3B5" ' + d.s('stroke-width="2.6"') + '/>'
    # хоккейная коробка
    b += '<rect x="30" y="50" width="60" height="54" rx="14" fill="#E6F7FF" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M30 77 H90" stroke="#E8464F" stroke-width="2.4"/><circle cx="60" cy="77" r="7" fill="none" stroke="#4E7BF2" stroke-width="2"/>'
    b += '<path d="M50 98 H70" stroke="#E8464F" stroke-width="2.4"/>'
    # схема: кружки и крестики, стрелка к воротам
    b += '<path d="M40 90 L44 94 M44 90 L40 94 M76 88 L80 92 M80 88 L76 92" stroke="#3B3355" stroke-width="2.2"/>'
    b += '<path d="M44 66 Q60 58 72 66 T60 94" fill="none" stroke="#3B3355" stroke-width="2.4" stroke-dasharray="4 3"/>'
    b += '<path d="M60 94 l-5 -5 M60 94 l6 -4" stroke="#3B3355" stroke-width="2.4" stroke-linecap="round"/>'
    b += d.face(60, 38, d=9, k=0.7)
    # маркер в «руке»
    b += '<path d="M98 54 Q108 50 112 40" fill="none" stroke="#3B3355" stroke-width="3" stroke-linecap="round"/>'
    b += '<rect x="106" y="20" width="9" height="24" rx="3" fill="#2DB37A" transform="rotate(20 110 32)" ' + d.s('stroke-width="2.4"') + '/>'
    save("hockey-masters-mosfilmovskaya", "green", b,
         "белый тренерский планшет с нарисованной хоккейной коробкой и лицом на зажиме",
         "сам чертит маркером пунктирную стрелку-комбинацию к воротам, как мастер разбора")


# 2. ДС «Борисоглебский» (Раменское): большой и маленький конёк катаются вместе
def borisoglebsky():
    b = '<path d="M0 96 Q64 86 128 96 V128 H0Z" fill="#F3FBFF" ' + d.s('stroke-width="2.4"') + '/>'
    # большой (взрослый) чёрный хоккейный
    b += ('<path d="M18 36 Q18 30 24 30 L42 30 Q48 30 48 36 L48 66 Q66 68 70 80 Q70 86 64 86 L22 86 Q16 86 16 80Z" '
          'fill="#2E3A55" ' + d.s() + '/>')
    b += d.face(38, 70, d=7, k=0.7)
    b += blade(16, 66, 94) + '<path d="M24 86 V92 M58 86 V92" stroke="#3B3355" stroke-width="3"/>'
    # маленький розовый фигурный
    b += ('<path d="M84 52 Q84 48 88 48 L100 48 Q104 48 104 52 L104 74 Q114 75 116 82 Q116 86 112 86 L86 86 Q82 86 82 82Z" '
          'fill="#FF9EC4" ' + d.s() + '/>')
    b += d.eye(91, 74, 0.6) + d.eye(100, 74, 0.6)
    b += '<path d="M92 79 Q95.5 82 99 79" fill="none" stroke="#3B3355" stroke-width="2"/>'
    b += blade(82, 112, 94) + '<path d="M88 86 V92 M106 86 V92" stroke="#3B3355" stroke-width="3"/>'
    # держатся шнурками
    b += '<path d="M48 40 Q66 30 84 54" fill="none" stroke="#F2C14E" stroke-width="3.2" stroke-linecap="round"/>'
    b += '<path d="M60 18 l3 -6 l3 6 l6 1 l-5 4 l2 6 l-6 -3 l-6 3 l2 -6 l-5 -4z" fill="#FFD45E" ' + d.s('stroke-width="1.8"') + '/>'
    save("rink-borisoglebsky-ramenskoe", "purple", b,
         "большой чёрный папин хоккейный конёк и маленький розовый детский фигурный",
         "катаются рядом по льду, держась друг за друга жёлтыми шнурками, как за руки")


# 3. Памп-трек «Фукусима» в Северном Чертанове: верблюжонок, у которого горбы — волны трека
def pump_chertanovo():
    b = '<path d="M0 104 H128 V128 H0Z" fill="#B98A5E"/>'
    # тело-трек: два горба
    b += '<path d="M8 104 Q26 104 34 84 Q44 58 56 84 Q62 96 70 84 Q80 58 92 84 Q98 104 120 104Z" fill="#E2B271" ' + d.s() + '/>'
    # шея и голова верблюжонка слева
    b += '<path d="M14 104 Q12 74 20 60 L30 60 Q24 78 30 100Z" fill="#E2B271" ' + d.s() + '/>'
    b += '<path d="M16 62 Q14 46 26 44 Q40 44 42 54 Q42 62 32 62 Z" fill="#E2B271" ' + d.s() + '/>'
    b += '<path d="M20 46 Q18 38 24 40" fill="#E2B271" ' + d.s('stroke-width="2.4"') + '/>'
    b += d.eye(28, 51, 0.65) + '<circle cx="39" cy="55" r="1.6" fill="#3B3355"/>'
    b += '<path d="M33 58 Q36 60 39 58" fill="none" stroke="#3B3355" stroke-width="2"/>'
    b += '<ellipse cx="24" cy="57" rx="3.5" ry="2" fill="#FF7FA8" opacity=".6"/>'
    # самокат на втором горбе
    b += '<g transform="rotate(-24 82 62)">'
    b += '<rect x="68" y="58" width="30" height="5" rx="2.5" fill="#4E7BF2" ' + d.s('stroke-width="2.2"') + '/>'
    b += '<path d="M94 58 L98 34 M92 34 H104" stroke="#3B3355" stroke-width="3.2" stroke-linecap="round"/>'
    b += '<circle cx="72" cy="66" r="5" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/><circle cx="96" cy="66" r="5" fill="#FFFFFF" ' + d.s('stroke-width="2.2"') + '/>'
    b += '</g>'
    b += '<path d="M104 46 q6 -4 12 0 M106 54 q6 -4 12 0" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round"/>'
    save("pumptrack-chertanovo-severnoe", "yellow", b,
         "песочный верблюжонок, чьи два горба — это волны асфальтового памп-трека",
         "терпеливо улыбается, пока по его второму горбу перелетает синий самокат")


ALL = [masters, borisoglebsky, pump_chertanovo]

if __name__ == "__main__":
    only = set(sys.argv[1:])
    for f in ALL:
        f()
    for pid, line in SUBJ.items():
        if not only or pid in only:
            print(line)
