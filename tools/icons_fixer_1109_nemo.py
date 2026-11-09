"""fixer 09.11: перерисовка cafe-druzya-nemo по сообщению Вадима («аватарка не подходит»)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cup(x, y, col, straw):
    # маленький детский стаканчик с полосатой трубочкой
    return f'''
<path d="M{x+4} {y-14} L{x+14} {y-34}" fill="none" {s('stroke-width="2.6"')}/>
<path d="M{x+4} {y-14} L{x+14} {y-34}" fill="none" stroke="{straw}" stroke-width="1.4" stroke-dasharray="3 3"/>
<path d="M{x-10} {y-18} L{x+10} {y-18} L{x+8} {y+6} L{x-8} {y+6}Z" fill="{col}" {s()}/>
<path d="M{x-9.4} {y-12} L{x+9.4} {y-12} L{x+8} {y+6} L{x-8} {y+6}Z" fill="#FFE45C" opacity=".95"/>
<path d="M{x-10} {y-18} L{x+10} {y-18} L{x+8} {y+6} L{x-8} {y+6}Z" fill="none" {s()}/>'''

body = f'''
<path d="M10 112 Q64 98 118 112 L118 130 L10 130Z" fill="#B98AE0" {s()}/>
{cup(38, 104, "#E9F7FF", "#FF5C7A")}
{cup(64, 106, "#E9F7FF", "#3FA9F5")}
{cup(90, 104, "#E9F7FF", "#4CC46A")}
<g transform="rotate(-28 70 46)">
 <path d="M50 22 L52 18 L90 18 L92 22 Q100 50 92 72 L50 72 Q42 50 50 22Z" fill="#EAF8FF" {s()}/>
 <path d="M46 36 Q44 54 50 70 L92 70 Q98 54 96 36Z" fill="#FFE45C"/>
 <path d="M50 22 L52 18 L90 18 L92 22 Q100 50 92 72 L50 72 Q42 50 50 22Z" fill="none" {s()}/>
 <path d="M50 22 L40 24 L48 30" fill="#EAF8FF" {s()}/>
 <path d="M93 30 Q112 34 108 50 Q104 62 92 60" fill="none" {s('stroke-width="5"')}/>
 <path d="M93 30 Q112 34 108 50 Q104 62 92 60" fill="none" stroke="#EAF8FF" stroke-width="2"/>
 <circle cx="60" cy="62" r="7" fill="#FFF7B0" {s('stroke-width="2.2"')}/>
 <path d="M60 55 L60 69 M53 62 L67 62" stroke="#E8C32A" stroke-width="1.6"/>
 <path d="M80 30 Q90 24 92 32 Q86 38 80 30Z" fill="#5CCB6A" {s('stroke-width="2.2"')}/>
 {face(71, 46, d=9, k=1.0)}
</g>
<path d="M32 44 Q30 64 37 88" fill="none" stroke="#3B3355" stroke-width="9" stroke-linecap="round"/>
<path d="M32 44 Q30 64 37 88" fill="none" stroke="#FFD43A" stroke-width="5" stroke-linecap="round"/>
<path d="M31 50 Q30 64 35 80" fill="none" stroke="#FFF7B8" stroke-width="1.6" stroke-linecap="round"/>
{sparkle(104, 82, 6)}{sparkle(20, 74, 4)}
'''
open(os.path.join(ROOT, "icons-src", "cafe-druzya-nemo.svg"), "w").write(svg("purple", body))
print("ok")
