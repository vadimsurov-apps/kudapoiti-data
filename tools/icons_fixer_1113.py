"""fixer 13.11: перерисовка иконки кинотеатра «Победа» (Зарайск) по сообщению Вадима «Аватар не подходит» (был самосвал)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, sparkle, O

body = f'''
<rect x="0" y="0" width="128" height="128" fill="#2E2752"/>
<path d="M118 128 L20 30 L108 22Z" fill="#FFF3B0" opacity=".28"/>
<rect x="16" y="20" width="96" height="58" rx="5" fill="#FFF8E2" {s()}/>
<path d="M44 74 Q40 60 52 54 L50 34 Q50 26 56 28 Q60 30 60 40 L61 50 L64 32 Q66 24 72 28 Q75 32 71 44 L68 54 Q82 58 80 74Z" fill="#4A3F7A"/>
<circle cx="62" cy="62" r="2.4" fill="#FFF8E2"/>
<path d="M66 68 Q70 71 74 67" fill="none" stroke="#FFF8E2" stroke-width="2.2" stroke-linecap="round"/>
<path d="M88 128 Q84 104 92 96 L90 80 Q90 74 95 75 Q99 76 99 84 L100 92 L103 78 Q105 72 110 75 Q113 78 110 88 L107 98 Q114 104 112 128Z" fill="#F9C9A8" {s()}/>
<path d="M96 108 Q100 106 104 108" fill="none" {s('stroke-width="2.2"')}/>
<rect x="0" y="100" width="80" height="28" fill="#8C2E4B" {s()}/>
<path d="M0 100 Q13 92 26 100 Q39 92 52 100 Q65 92 78 100" fill="#B23A5E" {s()}/>
{sparkle(28, 32, 4, "#FFD45E")}{sparkle(100, 30, 3, "#FFD45E")}
'''
icon = svg("night", body)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src", "pobeda-zaraysk.svg"), "w").write(icon)
print("ok")
