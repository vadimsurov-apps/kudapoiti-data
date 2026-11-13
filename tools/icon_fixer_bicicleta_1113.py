"""Fixer 13.11: перерисовка иконки cafe-la-bicicleta-dubna по сообщению Вадима «Аватар не подходит».
Якорь — блюдо заведения (в отзывах Яндекса хвалят карбонару «с желтком»), характер — желток-мордашка,
шутка — снежок тёртого сыра сверху."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import svg, s, eye, face, sparkle, O

pasta = ""
# горка спагетти
pasta += f'<path d="M22 88 Q20 58 44 50 Q64 40 84 50 Q108 58 106 88 Q64 104 22 88Z" fill="#FBE3A6" {s()}/>'
for d in ["M30 76 Q40 56 60 60 Q80 64 92 54", "M28 70 Q46 64 64 72 Q84 80 100 70",
          "M36 60 Q52 50 70 54 Q88 58 98 66", "M32 80 Q52 70 74 78 Q90 84 100 78",
          "M42 54 Q60 62 78 52"]:
    pasta += f'<path d="{d}" fill="none" stroke="#E8BF63" stroke-width="2.6" stroke-linecap="round"/>'
# кусочки бекона
for x, y in [(36, 66), (88, 62), (60, 76), (78, 74), (46, 76)]:
    pasta += f'<rect x="{x-4}" y="{y-3}" width="8" height="6" rx="2" fill="#E8735A" {s("stroke-width=\"1.8\"")}/>'
body = f'''
<ellipse cx="64" cy="94" rx="54" ry="20" fill="#2F6FD0" {s()}/>
<ellipse cx="64" cy="90" rx="44" ry="14" fill="#F4F8FF" {s('stroke-width="2.4"')}/>
{pasta}
<ellipse cx="64" cy="52" rx="19" ry="15" fill="#FFB524" {s()}/>
<ellipse cx="58" cy="46" rx="6" ry="3.5" fill="#FFE08A"/>
{eye(57, 53, 0.95)}
<path d="M66 53 Q70 50 74 53" fill="none" {s('stroke-width="2.6"')}/>
<path d="M61 59 Q65 63 69 59" fill="none" {s('stroke-width="2.4"')}/>
<ellipse cx="51" cy="60" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/>
<ellipse cx="78" cy="60" rx="3.6" ry="2.2" fill="#FF7FA8" opacity=".6"/>
'''
for x, y, r in [(40, 22, 2.6), (58, 16, 2.2), (76, 24, 2.8), (92, 18, 2.2), (48, 32, 2.0), (86, 34, 2.4), (68, 30, 1.8)]:
    body += f'<rect x="{x-r}" y="{y-r}" width="{2*r}" height="{2*r}" rx=".8" fill="#FFFBEA" stroke="#C9A64A" stroke-width="1.2" transform="rotate(20 {x} {y})"/>'
body += sparkle(104, 40, 5)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icons-src", "cafe-la-bicicleta-dubna.svg")
open(out, "w").write(svg("teal", body))
print("ok", out)
