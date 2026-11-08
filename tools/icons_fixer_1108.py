"""fixer 08.11: перерисовка иконки russian-alpacas по сообщению Вадима (была цесарка)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, O

FUR = "#9A5B34"; FUR2 = "#B8774A"
body = (
    # луг
    '<path d="M0 104 Q40 94 70 100 T128 98 V128 H0Z" fill="#7CCB5E" ' + s('stroke-width="2.6"') + '/>'
    # задние/передние ноги
    + '<g transform="translate(6,14) scale(0.88)">'
    + f'<path d="M34 92 V112 M46 94 V114 M70 94 V114 M80 92 V112" fill="none" stroke="{O}" stroke-width="9" stroke-linecap="round"/>'
    + f'<path d="M34 92 V112 M46 94 V114 M70 94 V114 M80 92 V112" fill="none" stroke="{FUR}" stroke-width="5" stroke-linecap="round"/>'
    # пушистое тело-облако
    + f'<path d="M24 80 Q18 68 28 64 Q30 54 42 56 Q48 48 58 54 Q68 48 76 56 Q88 54 88 66 Q96 72 90 82 Q92 94 80 94 '
      f'Q72 100 62 96 Q52 102 42 96 Q28 98 26 88 Q18 86 24 80Z" fill="{FUR2}" {s()}/>'
    # шея
    + f'<path d="M74 66 Q76 46 80 32 L96 32 Q94 50 90 70Z" fill="{FUR2}" {s()}/>'
    + f'<path d="M80 42 Q84 46 82 52 M86 56 Q90 60 88 66" fill="none" stroke="{FUR}" stroke-width="2.4" stroke-linecap="round"/>'
    # ушки
    + f'<path d="M80 18 Q76 4 82 2 Q86 8 86 18Z M92 18 Q94 4 100 4 Q100 12 96 20Z" fill="{FUR2}" {s("stroke-width=\"2.6\"")}/>'
    # голова (смотрит вправо)
    + f'<path d="M78 22 Q78 10 90 10 Q102 10 104 22 L112 28 Q116 36 108 40 Q98 42 92 38 Q80 38 78 22Z" fill="{FUR2}" {s()}/>'
    # хохолок
    + f'<path d="M80 16 Q78 6 86 8 Q88 2 94 6 Q100 4 100 12" fill="#D9A06E" {s("stroke-width=\"2.4\"")}/>'
    # мордочка
    + eye(94, 24, 0.9)
    + f'<ellipse cx="88" cy="31" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".65"/>'
    + f'<path d="M110 30 Q112 32 110 34" fill="none" {s("stroke-width=\"2\"")}/>'
    + f'<path d="M102 36 Q106 39 110 36" fill="none" {s("stroke-width=\"2.2\"")}/>'
    # ромашка во рту
    + f'<path d="M106 38 L114 50" fill="none" stroke="#3C8A3A" stroke-width="2.4" stroke-linecap="round"/>'
    + ''.join(f'<ellipse cx="{114+5*dx}" cy="{52+5*dy}" rx="3.2" ry="3.2" fill="#fff" {s("stroke-width=\"1.6\"")}/>'
              for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,-.7),(.7,-.7),(-.7,.7)])
    + f'<circle cx="114" cy="52" r="3.4" fill="#FFD23F" {s("stroke-width=\"1.6\"")}/>'
    # хвостик
    + f'<path d="M24 74 Q14 72 16 64 Q22 66 26 70" fill="{FUR2}" {s("stroke-width=\"2.6\"")}/>'
    + '</g>'
)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src", "russian-alpacas.svg"), "w").write(svg("orange", body))
