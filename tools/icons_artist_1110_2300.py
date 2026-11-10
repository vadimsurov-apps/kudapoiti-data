"""Робот «художник», 10.11 ~23:00 UTC.
check_unique.py: 4 пары похожих картинок (ребёнок-спортсмен в центре на розовом/оранжевом фоне):
princessa-rg-khodynka похожа сразу на три иконки, black-dragon-skobelevskaya ~ seiken-podolsk-yunykh-lenintsev.
Перерисованы princessa (царевна-лягушка и обруч) и seiken (бычок-каратист), остальные остаются.
Запуск из корня: python3 tools/icons_artist_1110_2300.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from draw_icons import s, eye, face, sparkle, O
from icons_artist_1106_2120 import W, bgsvg, blush, smile, ROOT

I = {}

# Клуб художественной гимнастики «Принцесса» (Ходынка) — царевна-лягушка прыгает сквозь золотой обруч
I["princessa-rg-khodynka"] = (
    "царевна-лягушка в маленькой золотой короне",
    "в длинном прыжке ныряет сквозь золотой гимнастический обруч, стоящий на ребре на синем ковре",
    ("#F4FBFF", "#7CC4E8"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#2F5FB3"/>
<path d="M0 104 H128" {W(2.6)}/>
<ellipse cx="66" cy="106" rx="20" ry="3" fill="#1E3F80" opacity=".6"/>
<circle cx="66" cy="66" r="38" fill="none" {W(10)}/>
<circle cx="66" cy="66" r="38" fill="none" stroke="#FFC93C" stroke-width="6"/>
<path d="M44 36 A38 38 0 0 1 88 36" fill="none" stroke="#FFF1B8" stroke-width="2" stroke-linecap="round"/>
<path d="M30 80 Q16 86 10 98" fill="none" {W(8)}/><path d="M30 80 Q16 86 10 98" fill="none" stroke="#5DBB4A" stroke-width="4.4" stroke-linecap="round"/>
<path d="M34 86 Q24 96 22 104" fill="none" {W(8)}/><path d="M34 86 Q24 96 22 104" fill="none" stroke="#5DBB4A" stroke-width="4.4" stroke-linecap="round"/>
<ellipse cx="9" cy="99" rx="5" ry="3" fill="#5DBB4A" {W(2.2)}/>
<ellipse cx="21" cy="105" rx="5" ry="3" fill="#5DBB4A" {W(2.2)}/>
<path d="M30 84 Q40 62 66 60 Q88 60 96 72 Q90 88 64 90 Q42 92 30 84Z" fill="#5DBB4A" {W(3.2)}/>
<path d="M44 84 Q62 88 84 80 Q74 88 60 89 Q50 89 44 84Z" fill="#C9EE9C"/>
<path d="M88 72 Q100 64 108 56" fill="none" {W(7)}/><path d="M88 72 Q100 64 108 56" fill="none" stroke="#5DBB4A" stroke-width="3.6" stroke-linecap="round"/>
<circle cx="110" cy="54" r="3.6" fill="#5DBB4A" {W(2)}/>
<circle cx="78" cy="58" r="8.5" fill="#5DBB4A" {W(3)}/>
<circle cx="94" cy="62" r="8.5" fill="#5DBB4A" {W(3)}/>
{eye(78, 58, .7)}{eye(94, 62, .7)}
{blush(76, 72, .6)}
<path d="M80 76 Q88 80 96 74" fill="none" {W(2.2)}/>
<path d="M76 50 L78 40 L82 46 L86 38 L89 47 L94 42 L94 53 Q85 50 76 50Z" fill="#FFC93C" {W(2.4)}/>
<circle cx="86" cy="45" r="1.6" fill="#E8455B"/>
{sparkle(108, 24, 5)}{sparkle(22, 30, 3.5)}{sparkle(116, 92, 3)}''')

# Клуб киокусинкай «Сэйкен» (Подольск) — бычок-каратист в стойке всадника кричит «киай»
I["seiken-podolsk-yunykh-lenintsev"] = (
    "коричневый бычок с маленькими рожками в белом кимоно с оранжевым поясом",
    "стоит в широкой стойке всадника на тёмно-зелёном татами, кулаки у пояса, и громко выдыхает «киай!» — от рта разлетаются чёрточки",
    ("#E6F4F1", "#2F8C83"), f'''
<path d="M0 104 H128 V128 H0Z" fill="#245E3A"/>
<path d="M0 104 H128 M44 104 V128 M88 104 V128" {W(2.4)}/>
<path d="M30 78 Q22 92 16 102 L32 104 Q38 94 44 86Z" fill="#FFFFFF" {W(3)}/>
<path d="M98 78 Q106 92 112 102 L96 104 Q90 94 84 86Z" fill="#FFFFFF" {W(3)}/>
<ellipse cx="22" cy="104" rx="9" ry="4" fill="#6B4024" {W(2.4)}/>
<ellipse cx="106" cy="104" rx="9" ry="4" fill="#6B4024" {W(2.4)}/>
<path d="M42 56 Q64 50 86 56 L90 84 Q64 90 38 84Z" fill="#FFFFFF" {W(3.2)}/>
<path d="M54 54 L64 72 L74 54" fill="none" {W(2.4)}/>
<path d="M38 74 Q64 80 90 74 L90 81 Q64 87 38 81Z" fill="#FF8A1F" {W(2.6)}/>
<path d="M62 80 L56 94 M66 80 L72 94" {W(5)}/><path d="M62 80 L56 94 M66 80 L72 94" stroke="#FF8A1F" stroke-width="2.4" stroke-linecap="round"/>
<path d="M42 60 Q30 66 32 76" fill="none" {W(10)}/><path d="M42 60 Q30 66 32 76" fill="none" stroke="#FFFFFF" stroke-width="6.4" stroke-linecap="round"/>
<path d="M86 60 Q98 66 96 76" fill="none" {W(10)}/><path d="M86 60 Q98 66 96 76" fill="none" stroke="#FFFFFF" stroke-width="6.4" stroke-linecap="round"/>
<circle cx="33" cy="78" r="5.5" fill="#6B4024" {W(2.6)}/>
<circle cx="95" cy="78" r="5.5" fill="#6B4024" {W(2.6)}/>
<path d="M48 26 Q36 24 32 12 Q44 16 52 22Z" fill="#FFE7B0" {W(2.6)}/>
<path d="M80 26 Q92 24 96 12 Q84 16 76 22Z" fill="#FFE7B0" {W(2.6)}/>
<ellipse cx="38" cy="32" rx="8" ry="4.5" fill="#8A5530" {W(2.6)}/>
<ellipse cx="90" cy="32" rx="8" ry="4.5" fill="#8A5530" {W(2.6)}/>
<ellipse cx="64" cy="36" rx="20" ry="19" fill="#8A5530" {W(3.2)}/>
<path d="M56 20 Q60 14 64 20 Q68 14 72 20" fill="none" {W(2.4)}/>
<path d="M50 28 L58 32 M78 28 L70 32" {W(2.4)}/>
{eye(56, 36, .62)}{eye(72, 36, .62)}
<ellipse cx="64" cy="48" rx="13" ry="8.5" fill="#E9B98E" {W(2.6)}/>
<ellipse cx="58" cy="46" rx="1.8" ry="2.4" fill="{O}"/><ellipse cx="70" cy="46" rx="1.8" ry="2.4" fill="{O}"/>
<ellipse cx="64" cy="52.5" rx="4.5" ry="2.6" fill="#7A2730" {W(1.8)}/>
<path d="M84 50 L96 46 M85 56 L98 58 M44 50 L32 46 M43 56 L30 58" {W(2.4)}/>
{sparkle(112, 26, 4.5)}''')

if __name__ == "__main__":
    for pid, (hero, scene, (a, b), body) in I.items():
        open(os.path.join(ROOT, "icons-src", f"{pid}.svg"), "w").write(bgsvg(a, b, body))
    reg = os.path.join(ROOT, "icons-src", "subjects.txt"); txt = open(reg, encoding="utf-8").read()
    for pid in I:
        txt = re.sub(rf"^{re.escape(pid)} — .*\n", "", txt, flags=re.M)
    if not txt.endswith("\n"):
        txt += "\n"
    txt += "".join(f"{pid} — герой: {h} | сцена: {sc}\n" for pid, (h, sc, _, _) in I.items())
    open(reg, "w", encoding="utf-8").write(txt)
    print(" ".join(I))
